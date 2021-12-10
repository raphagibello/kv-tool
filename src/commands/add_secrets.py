import os
import cmd
import csv
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,AzureCliCredential
import click

def register_commands(group):
    group.add_command(add_single)
    group.add_command(hello)
    group.add_command(add_list)
    group.add_command(clone_keyvault)
    group.add_command(list_secrets)
    group.add_command(list_secret_names)
    
@click.command()
def hello():
    click.echo('Hello World!')

@click.command()
@click.option('--keyvault_name', '-kv')
@click.option('--secret_name', '-n') 
@click.option('--secret_value', '-v')
def add_single(keyvault_name, secret_name, secret_value):
    '''
    add_single is designed to add a single secret to a Key Vault.
    '''
    credential = AzureCliCredential()
    keyvault_name = keyvault_name
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)
    print(f"Creating a secret in {keyvault_name} called '{secret_name}' ...")   
    kv_client.set_secret(secret_name, secret_value)

@click.command()
@click.option('--keyvault_name', '-kv')
@click.option('--csv_file', '-csv') 
def add_list(keyvault_name,csv_file):
    credential = AzureCliCredential()
    keyvault_name = keyvault_name
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)
    with open(csv_file,"r") as secrets_csv:
        csv_reader = csv.reader(secrets_csv, delimiter=";")
        for row in csv_reader:
            csv_secret_name = row[0]
            csv_secret_value = row[1]
            print(f"Creating a secret in {keyvault_name} called '{csv_secret_name}' ...")
            kv_client.set_secret(csv_secret_name, csv_secret_value)

@click.command()
@click.option('--keyvault_name', '-kv')
@click.option('--source_keyvault_name', '-skv')
def clone_keyvault(keyvault_name,source_keyvault_name):
    name_secret_dict = {}
    credential = AzureCliCredential()
    keyvault_name = keyvault_name
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)
    secrets_list = list_secrets(source_keyvault_name)

    for secret_name in secrets_list:
        secret = kv_client.get_secret(secret_name)
        name_secret_dict[secret.name] = [secret.value]

    for key in name_secret_dict.keys():
        kv_client.set_secret(key, name_secret_dict[key])
       
@click.command()
@click.option('--keyvault_name', '-kv')
def list_secret_names(keyvault_name):
    secrets_list = []
    credential = AzureCliCredential()
    keyvault_name = keyvault_name
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)
    secret_properties = kv_client.list_properties_of_secrets()

    for secret_property in secret_properties:
        print(secret_property.name)
        secrets_list.append(secret_property.name)
    return secrets_list

@click.command()
@click.option('--keyvault_name', '-kv')
def list_secrets(keyvault_name):
    name_secret_dict = {}
    secrets_list = []


    credential = AzureCliCredential()
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    kv_client = SecretClient(vault_url=KVUri, credential=credential)

    secret_properties = kv_client.list_properties_of_secrets()

    for secret_property in secret_properties:
        secrets_list.append(secret_property.name)

    for secret_name in secrets_list:
        secret = kv_client.get_secret(secret_name)
        name_secret_dict[secret.name] = [secret.value]

    for key in name_secret_dict.keys():
        print(key + ";" + name_secret_dict[key][0])

