import socket
import ssl
import os

def send_file(host, port, file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    with open(file_path, 'r') as file:
        file_content = file.read()

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('cert.pem')

    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(file_content.encode())

if __name__ == "__main__":
    target_host = "192.168.0.220"  # Replace with the server's IP address
    target_port = 12345
    
    while True:
        file_path = input("Enter the file path to send (or type 'exit' to quit): ")
        if file_path.lower() == 'exit':
            break
        send_file(target_host, target_port, file_path)

