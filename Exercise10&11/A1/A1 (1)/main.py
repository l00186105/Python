"""
main.py
By: JMC
Date: 20OCT23
"""
# Detect OS and workng directory
from directory_utilities import detect_os, detect_working_directory
print(detect_os())
print(detect_working_directory())        
print
from file_utilities import path_name, log_file_name
from os_utilities import detect_os

# define path
from mypaths import UDP_SETTINGS as udp_settings
print(udp_settings)

# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".csv")
print(log_path + filename )
