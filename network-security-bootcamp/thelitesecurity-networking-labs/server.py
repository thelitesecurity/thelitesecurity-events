import socket
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import pickle

# Generate server's public and private keys
private_key_server = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key_server = private_key_server.public_key()

# Serialize server's public key
serialized_public_key_server = public_key_server.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Start server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening...")

# Accept client connection
client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Send server's public key to the client
client_socket.send(serialized_public_key_server)

# Receive client's public key
serialized_public_key_client = client_socket.recv(4096)
public_key_client = serialization.load_pem_public_key(serialized_public_key_client)

# Communication loop
while True:
    # Get user input to send to the client
    message = input("Enter message to send (or type 'exit' to quit): ")
    
    # Encrypt the message with the client's public key
    encrypted_message = public_key_client.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Send encrypted message to client
    client_socket.send(encrypted_message)
    
    if message.lower() == 'exit':
        break

client_socket.close()
server_socket.close()
