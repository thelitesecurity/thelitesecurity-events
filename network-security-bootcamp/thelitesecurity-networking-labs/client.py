import socket
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import pickle

# Generate client's public and private keys
private_key_client = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key_client = private_key_client.public_key()

# Serialize client's public key
serialized_public_key_client = public_key_client.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Send client's public key to the server
client_socket.send(serialized_public_key_client)

# Receive server's public key
serialized_public_key_server = client_socket.recv(4096)
public_key_server = serialization.load_pem_public_key(serialized_public_key_server)

# Communication loop
while True:
    # Receive encrypted message from the server
    encrypted_message = client_socket.recv(4096)
    
    # Decrypt the message using client's private key
    decrypted_message = private_key_client.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()
    
    print(f"Received message: {decrypted_message}")
    
    if decrypted_message.lower() == 'exit':
        break

client_socket.close()

