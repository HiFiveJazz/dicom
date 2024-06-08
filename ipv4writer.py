
def writeipaddress():
    with open('cert_config.cnf', 'r') as file:
        lines = file.readlines()
    line_number = 23
    if len(lines) >= line_number:
# Editing cert_config.cnf
        ipaddress = input("Please enter the Receiving Computer's IP Address: ")
        lines[22] = 'IP.1   = '+ ipaddress + '\n' 
        with open('cert_config.cnf', 'w') as file:
            file.writelines(lines)
# Editing Sender.py
        with open('sender.py', 'r') as file:
            lines = file.readlines()
        lines[22] = '    target_host = "'+ ipaddress +'"\n'
        with open('sender.py', 'w') as file:
            file.writelines(lines)
        return ipaddress

def write_ipaddress_sender():
    with open('cert_config.cnf', 'r') as file:
        lines = file.readlines()
    line_number = 23
    if len(lines) >= line_number:
# Editing cert_config.cnf
        ipaddress = input("Please enter the Receiving Computer's IP Address: ")
        lines[22] = 'IP.1   = '+ ipaddress + '\n' 
        with open('cert_config.cnf', 'w') as file:
            file.writelines(lines)
# Editing Sender.py
        return ipaddress
