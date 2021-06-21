from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,AzureCliCredential
from commands import add_secrets
import csv
import click

def register_commands(group):
    group.add_command(remove_single)
    group.add_command(remove_list)
    group.add_command(clean_keyvault)

@click.command()
@click.option('--keyvault_name', '-kv')
@click.option('--secret_name', '-n') 
def remove_single(keyvault_name,secret_name):
    credential = AzureCliCredential()
    keyvault_name = keyvault_name
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)
    deleted_secret = kv_client.begin_delete_secret(secret_name).result()

@click.command()
@click.option('--keyvault_name', '-kv')
@click.option('--csv_file', '-csv')
def remove_list(keyvault_name,csv_file):
    credential = AzureCliCredential()
    keyvault_name = keyvault_name
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)

    with open(csv_file,"r") as secrets_csv:
        csv_reader = csv.reader(secrets_csv, delimiter=";")
        for row in csv_reader:
            csv_secret_name = row[0]
            csv_secret_value = row[1]
            print(f"Deleting a secret in {keyvault_name} called '{csv_secret_name}' ...")
            deleted_secret = kv_client.begin_delete_secret(csv_secret_name).result()
            print(f"Secret '{deleted_secret.name}' deleted")
            
@click.command()
@click.option('--keyvault_name', '-kv')
def clean_keyvault(keyvault_name):
    credential = AzureCliCredential()
    keyvault_name = keyvault_name
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)
    secrets_list = add_secrets.list_secrets(keyvault_name)

    for secret_name in secrets_list:
            deleted_secret = kv_client.begin_delete_secret(secret_name).result()
            print(f"Secret '{deleted_secret.name}' deleted")
       
