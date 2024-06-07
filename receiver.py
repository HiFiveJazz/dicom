import socket
import ssl
import json
from blockchain import Blockchain

def save_file(file_content, filename='received_file.txt'):
    with open(filename, 'w') as file:
        file.write(file_content)

def start_server(host='0.0.0.0', port=12345):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        with context.wrap_socket(server_socket, server_side=True) as ssock:
            chain = Blockchain(difficulty=4)
            while True:
                client_socket, client_address = ssock.accept()
                print(f"Connection from {client_address}")
                file_content = client_socket.recv(65536).decode()
                print(f"Received file content:\n{file_content}")
                
                # Add file content to blockchain
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
    start_server()

