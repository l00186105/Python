'''
UDPServer by: JMC
Listens for packets on the address and port in the settings file for A1 project.
Alpha: 14NOV23
'''

import socket
import settings.udp as settings

UDP_IP = settings.udp["SERVER_UDP_IPv4"]
UDP_PORT = settings.udp["SERVER_PORT"]
BUFFER_SIZE = 1024

print(f'This is the UDP server for A1 project, it will open a port at {UDP_IP}:{UDP_PORT} and start listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print('listening for temperature, timestamp and senor ID')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind( (UDP_IP, UDP_PORT) )
    print('Listening on', UDP_IP)
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        data = data.decode()
        print(addr, data)
