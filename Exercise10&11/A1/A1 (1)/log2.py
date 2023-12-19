""""
Logging programme
By: JMC
Date: Nov 19 2023   
"""
from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load
from time import sleep

import socket
import time
from datetime import datetime
import settings.udp as settings

UDP_IP = settings.udp["SERVER_UDP_IPv4"]
UDP_PORT = settings.udp["SERVER_PORT"]

print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')


# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".csv")
print(log_path + filename)

# Loop forever
while True:
    # Sleep for 5 seconds
    sleep(5)
    # Get a time stamp for this line
    timestamp = log_file_name("")
    # Get some information
    information = cpu_load()
    # Create a line for the logfile, convert the integer values to string
    logline = timestamp + ":" + str(information) + "\n"
   
   
    



