import socket
import os

def send_file(host, port, file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    with open(file_path, 'r') as file:
        file_content = file.read()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(file_content.encode())
    client_socket.close()

if __name__ == "__main__":
    target_host = "192.168.0.210"  # Replace with the server's IP address
    target_port = 12345
    
    while True:
        file_path = input("Enter the file path to send (or type 'exit' to quit): ")
        if file_path.lower() == 'exit':
            break
        send_file(target_host, target_port, file_path)

