# Block Chain Messaging System

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Introduction
This project is a proof of concept for Bioengineering 193 at UC San Diego. It demonstrates a basic Peer-to-Peer blockchain messaging system, similar to how Radiologists transfer DICOM files. By implementing a blockchain system, we aim to enhance cybersecurity for Radiologists.

This project creates a basic client-server application for sending text files over a network with a ledger system similar to that of Bitcoin. The server, written in Python, can send a text file to a client, which receives and displays the content. The instructions below will guide you through setting up and running the project on two computers: one acting as the server and the other as the client.

The project is divided into several steps:

1. **Setting Up the Server and Client**: Configuring the IP addresses and ensuring both systems can communicate.
2. **Modifying the Server Script**: Updating the server script (`sender.py`) with the correct IP address of the client.
3. **Running the Application**: Executing the scripts on both the client and server computers to transfer a text file.

## Installation
***Clone the repository:***
```bash
git clone https://github.com/HiFiveJazz/dicom.git
```
## Usage

In order to send messages via the block chain, 
- Ensure both the both devices are connected to the same network (this code uses Peer-to-Peer protocol)
- Designate one computer as the **Client** and the other as the **Server**.

### Step 1: Find Two Computers
You need two computers, one to act as the receiving computer (server) and one to act as the sending computer (client). Alternatively, you could use set up a virtual machine on a single computer and attempt sending the message between the virtual machine and real computer, but this has not been tested.


**macOS Example:**

```bash
ifconfig
```
Search for the IPv4 address shown after en0:

```bash
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether f8:4d:89:63:de:0f
	inet6 fe80::472:9e9:6f51:55df%en0 prefixlen 64 secured scopeid 0xe 
	inet 192.168.0.210 netmask 0xffffff00 broadcast 192.168.0.255
	inet6 2600:8801:8101:9800:859:c401:d449:459b prefixlen 64 autoconf secured 
	inet6 2600:8801:8101:9800:6419:a335:9c55:755b prefixlen 64 autoconf temporary 
	inet6 2600:8801:8101:9800::de98 prefixlen 64 dynamic 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
```

*IPv4 Address = 192.168.0.210*

**Linux Example:**

```bash
nmcli -p device show
```
```bash
===============================================================================
                            Device details (enp6s0)
===============================================================================
GENERAL.DEVICE:                         enp6s0
-------------------------------------------------------------------------------
GENERAL.TYPE:                           ethernet
-------------------------------------------------------------------------------
GENERAL.HWADDR:                         11:22:3A:F4:55:6F
-------------------------------------------------------------------------------
GENERAL.MTU:                            1500
-------------------------------------------------------------------------------
GENERAL.STATE:                          100 (connected)
-------------------------------------------------------------------------------
GENERAL.CONNECTION:                     Wired connection 1
-------------------------------------------------------------------------------
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConne>
-------------------------------------------------------------------------------
WIRED-PROPERTIES.CARRIER:               on
-------------------------------------------------------------------------------
IP4.ADDRESS[1]:                         192.168.0.220/24
```

*IPv4 Address = 192.168.0.220*

### Step 2: On the Server Computer, replace Line 18 in `sender.py` with the IPv4 Address of the Client
```python
if __name__ == "__main__":
    target_host = "192.168.0.210"  # Replace with the server's IP address
    target_port = 12345
```

### Step 3: Running the Program

#### On the Client Computer:
Run the following command:
```bash
python3 receiver.py
```

#### On the Server Computer:

1. Create a new '.txt' file to send to the Client with some text inside:

```bash
nvim hello.txt
```
2. Add any text to 'hello.txt'

```hello.txt
This is some test text
```

3. Run 'sender.py':

```bash
python3 sender.py
```

4. Input the name of the file when prompted

```bash
hello.txt
```

You're done!

## Contact
Feel free to contact me at jasmeet.bhatia.us@gmail.com if you have any questions!
