#Running Linux terminal Commands using Python

# Terminal Commands can be executed by using two modules os or subprocess.
#Lets first implement with os module.

import os

x= os.system("date")
#This will run the date command.But it stores only  the exit code of the command and displays the date command .Exit code conatins value whether the command is successfully executed or not
#If exit code is 0 , then it is successfull executed else not.
#But if we want to store the output of the command as well the exit code we use subprocess module.
#Subprocess behind the scene uses tuple to store both the exit code and the output.

import subprocess 
y = subprocess.getstatusoutput("date")
#storing the exit code in variable status
status =y[0]
#storing the output in variable out
out =y[1]
