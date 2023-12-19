#IAC Assignment 1 Project#
This sheet contains summary information for the **IAC Assignment 1** project. 

The contents are as follows:

1. overview of the project
2. batch files information for automating the structure of the project
3. main.py programme in the project root

##Overview of the project##
This project provides a solution to a farmer who needs to transmit sensor data to a receiving server. The project includes a simulator to demonstrate the data flow, three UDP clients to unicast a single temperature to a server, with a time stamp and a sensor ID, and separate log files. 

###batch file information for automating the structure of the project###
The set up of this project was automate using the following batch file:
project_setup.bat

The code inside this batch file is as folows:
```python
@@echo off
cls
echo "**********************************************"
echo This batch file creates the project directory structure for IAC Assignment1 project A1 by JMC
echo "**********************************************"
echo *** press [ctrl][c] to exit or any key to continue ***
pause 
set /p NAME=Enter the name of the project, then press [return]  
echo Creating %NAME%
mkdir %NAME%
cd %NAME%
mkdir Documentation
mkdir Tests
mkdir Examples
mkdir Source
cls
dir
echo "**********************************************"
echo Finished creating project %NAME%
echo "**********************************************"
cd ..
```

####main.py programme in the project root####

The main programme code for this project is as follows:

```python
"""
main.py
By: JMC
Date: 05NOV2023
"""

from Source.directory_utilities import detect_os, detect_working_directory
print(detect_os())
print(detect_working_directory())        
```



