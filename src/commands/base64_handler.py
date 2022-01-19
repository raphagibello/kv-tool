import base64
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,AzureCliCredential
import click

def encode_line(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode((message_bytes))
    base64_message = base64_bytes.decode('ascii')

    return base64_message  # returns the encoded String

def encode_file():
    with open('random.txt', 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')
        print(base64_message)

def decode_line(message):
    encoded = encode_line(message)  #encoded String
    base64_message = encoded
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    return message  #returns the decoded String

def decode_file(key):
    base64_img_bytes = key.encode('utf-8')
    with open('random.txt', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

# with open("secrets_k8s_decoded.txt","r") as decoded_file:
#     for line in decoded_file:
#         stripped_line = line.strip()
#         print("Decoded String: " + stripped_line)
#         stripped_line_bytes = stripped_line.encode('ascii')
#         base64_bytes = base64.b64encode(stripped_line_bytes)
#         base64_message = base64_bytes.decode('ascii')
#         print("Encoded String: " + base64_message)