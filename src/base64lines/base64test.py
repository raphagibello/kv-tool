import base64

print('Say something: ')
message = input()


def encode_line(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode((message_bytes))
    base64_message = base64_bytes.decode('ascii')

    return base64_message  # returns the encoded String


print("Encoded line: " + encode_line(message))


def decode_line(message):
    encoded = encode_line(message)  #encoded String
    base64_message = encoded
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    return message  #returns the decoded String


print("Decoded line: " + decode_line(message))
