'''
UDPClient2 by: JMC
Send UDP packets with temperature and timestamp data to the address and port for the A1 project  
Date: 20OCT23
'''

import socket
import time
from datetime import datetime
import settings.udp2 as settings

UDP_IP = settings.UDP2["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP2["SERVER_PORT"]

print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')
print('This script has no error handling, by design')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message_text = f"Temp2,16C,{datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (UDP_IP, UDP_PORT))
        print(f'Sent {message_text}')
        time.sleep(5)
