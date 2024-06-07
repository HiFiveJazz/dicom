import socket
import json
from blockchain import Blockchain

def save_file(file_content, filename='received_file.txt'):
    with open(filename, 'w') as file:
        file.write(file_content)

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    chain = Blockchain(difficulty=4)

    while True:
        client_socket, client_address = server_socket.accept()
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


