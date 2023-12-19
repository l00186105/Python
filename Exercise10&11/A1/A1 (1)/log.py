""""
Logging programme
By: JMC
Date: Nov 19 2023   
"""
from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load
from time import sleep


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
    logline = timestamp + ":" + str(information) + "," + "\n"
    # Now write it to the logfile
    



