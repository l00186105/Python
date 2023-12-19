@echo off
cls
title JMC's first script
echo "*******************************************"
echo This is the first line of my batch file for demo 2
echo This is the second line of my batch file for demo 2.
echo "*******************************************"
echo
echo *** About to do something critical ***
echo *** press [ctrl][c] to exit or any key to continue ***
pause 
SETLOCAL

SET clonepath=V:\Clone of UB1604-Server\
SET clonename=UB1604-04JAN18.vmx
echo Path to Clone is %clonepath%%clonename%

SET /A calculation=2+12/4
echo We got %calculation%

ENDLOCAL

EXIT