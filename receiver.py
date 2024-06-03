import socket
import json
from blockchain import Blockchain

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    chain = Blockchain()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        
        # Add message to blockchain
        chain.add_block(message)
        chain.display_chain()
        print(f"Is chain valid? {chain.verify_chain()}")
        
        # Print the entire ledger
        ledger = chain.get_ledger()
        print(json.dumps(ledger, indent=4))

        client_socket.close()

if __name__ == "__main__":
    start_server()

