import base64
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,AzureCliCredential
import click

def encode_line():
    return 0

def encode_file():
    return 0

def decode_line():
    return 0

def decode_file():
    return 0

# with open("secrets_k8s_decoded.txt","r") as decoded_file:
#     for line in decoded_file:
#         stripped_line = line.strip()
#         print("Decoded String: " + stripped_line)
#         stripped_line_bytes = stripped_line.encode('ascii')
#         base64_bytes = base64.b64encode(stripped_line_bytes)
#         base64_message = base64_bytes.decode('ascii')
#         print("Encoded String: " + base64_message)