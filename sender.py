import socket

def send_message(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(message.encode())
    client_socket.close()

if __name__ == "__main__":
    target_host = "192.168.0.210"  # Replace with the server's IP address
    target_port = 12345
    
    while True:
        message = input("Enter the message to send (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        send_message(target_host, target_port, message)
