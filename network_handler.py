def get_local_ipv4_address():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception as e:
        local_ip = None
        print(f"Error occurred: {e}")
    finally:
        s.close()
    print(f"Local IP Address: {local_ip}")
    return local_ip

def write_ipv4_address_receiver(ipaddress):
    with open('cert_config.cnf', 'r') as file:
        lines = file.readlines()
    line_number = 23
    if len(lines) >= line_number:
# Editing cert_config.cnf
        lines[22] = 'IP.1   = '+ ipaddress + '\n' 
        with open('cert_config.cnf', 'w') as file:
            file.writelines(lines)


def generate_self_signed_cert(config_file='cert_config.cnf', key_file='key.pem', cert_file='cert.pem'):
    import subprocess
    command = [
        'openssl', 'req', '-x509', '-nodes', '-days', '365', 
        '-newkey', 'rsa:2048', '-keyout', key_file, 
        '-out', cert_file, '-config', config_file
    ]

    try:
        with open('/dev/null', 'w') as devnull:
            subprocess.run(command, check=True, stdout=devnull, stderr=devnull)
        print(f"Certificate and key have been successfully generated: {cert_file}, {key_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
