import socket
import ssl
import os

def request_cert_file(host, port, certfile='cert.pem'):
    with socket.create_connection((host, port)) as sock:
        sock.sendall('REQUEST_CERT'.encode())
        cert_content = sock.recv(65536).decode()
        with open(certfile, 'w') as file:
            file.write(cert_content)
    print(f"Received cert.pem from {host}")

def send_file(host, port, file_path, certfile='cert.pem'):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    with open(file_path, 'r') as file:
        file_content = file.read()

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(certfile)

    with socket.create_connection((host, port)) as sock:
        sock.sendall('SEND_FILE'.encode())
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(file_content.encode())

if __name__ == "__main__":
    target_host = input("Input Server IP Address: \n") 
    target_port = 12345
    
    # Step 1: Request the cert.pem file from the receiver
    request_cert_file(target_host, target_port)
    
    # Step 2: Send the file securely using the received cert.pem
    while True:
        file_path = input("Enter the file path to send (or type 'exit' to quit): ")
        if file_path.lower() == 'exit':
            break
        send_file(target_host, target_port, file_path)

