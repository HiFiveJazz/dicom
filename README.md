# Block Chain Messaging System

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Introduction
This project is a proof of concept for BENG 193: Clinical Bioengineering at UC San Diego. It demonstrates a basic Peer-to-Peer blockchain messaging system, similar to how Radiologists can transfer DICOM files. By implementing a blockchain system, we aim to enhance cybersecurity for Radiologists or other healthcare specialists alike.

This project creates a basic client-server application for sending text files over a network with a ledger system similar to that of Bitcoin. The server, written in Python, can send a text file to a client, which receives and displays the content. The instructions below will guide you through setting up and running the project on two computers: one acting as the server and the other as the client.

The project is divided into several steps:

1. **Designating Computers as the Server and Client**: By setting designating computers, it allows for the following steps to be easy to follow
2. **Running the Application**: Executing the scripts on both the client and server computers to transfer a text file over.

## Installation
***Clone the repository:***
```bash
git clone https://github.com/HiFiveJazz/dicom.git
```
## Usage

In order to send messages via the block chain, 
- Ensure both the both devices are connected to the same network (this code uses Peer-to-Peer protocol along with a TLS handshake between the devices through an open port (default port is 12345)).
- Designate one computer as the **Client** and the other as the **Server**.

### Step 1: Find Two Computers
You need two computers, one to act as the receiving computer (server) and one to act as the sending computer (client). Alternatively, you could use set up a virtual machine on a single computer and attempt sending the message between the virtual machine and real computer, but this has not been tested.

### Step 2: Ensure Network Compatibility
This program uses the TLS and Peer-to-Peer protocols for sending encrypted text files between one another, allowing the creation of the blockchain. In order for this to work, ensure both computers are connected to the same Wi-Fi network. Also, ensure the network doesn't have the a firewall that blocks the port for sending files on the network. If it does, consider either changing the port on which you send the files through by editing `sender.py` and `receiver.py` or Port Forward the desired port through your network.  

### Step 3: Running the Program

#### On the Server Computer:
Run the `receiver.py` file:
```bash
cd dicom
python3 receiver.py
```
Note what IP Address is shown after running the command, you will need to give this to the sending computer.

Example Output:

```bash
IP Address: 192.168.0.210
Listening on 0.0.0.0:12345
```
#### On the Client Computer:

1. Run the `sender.py` file:
```bash
cd dicom
python3 sender.py
```

2. Enter in the IP Address of the Server Computer, shown before 

```bash
192.168.0.210
```

3. Create a text file and give it to send to the Server. Submit the file path of the created text file when prompted (by default, type example.txt).

```bash
example.txt
```
You're done!
## License
This project uses the GNU GPLv3 License so do what you want, as long as it is open-source.

## Contact
Feel free to contact me at jasmeet.bhatia.us@gmail.com if you have any questions!
