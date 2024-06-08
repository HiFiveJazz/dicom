import socket
import ssl
import json
import os
from blockchain import Blockchain
import ipv4writer

def save_file(file_content, filename='received_file.txt'):
    with open(filename, 'w') as file:
        file.write(file_content)

def send_cert_file(client_socket, certfile='cert.pem'):
    with open(certfile, 'r') as file:
        cert_content = file.read()
    client_socket.sendall(cert_content.encode())

def start_server(host='0.0.0.0', port=12345):
    certfile = os.getenv('CERT_FILE', 'cert.pem')
    keyfile = os.getenv('KEY_FILE', 'key.pem')
    
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            request_type = client_socket.recv(1024).decode()

            if request_type == 'REQUEST_CERT':
                print(f"Sending cert.pem to {client_address}")
                send_cert_file(client_socket, certfile)
            elif request_type == 'SEND_FILE':
                with context.wrap_socket(client_socket, server_side=True) as ssock:
                    file_content = ssock.recv(65536).decode()
                    print(f"Received file content:\n{file_content}")
                    
                    # Add file content to blockchain
                    chain = Blockchain(difficulty=4)
                    chain.add_block(file_content)
                    chain.display_chain()
                    print(f"Is chain valid? {chain.verify_chain()}")
                    
                    # Save the received file
                    save_file(file_content)
                    
                    # Print the entire ledger
                    ledger = chain.get_ledger()
                    print(json.dumps(ledger, indent=4))

            client_socket.close()

if __name__ == "__main__":
    
    local_ip = ipv4writer.get_local_ipv4_address()
    ipv4writer.write_ipv4_address_receiver(local_ip)
    ipv4writer.generate_self_signed_cert()
    start_server()

