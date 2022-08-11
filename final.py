#!/bin/python

import subprocess
import os
import time

while True:
    for subdir, dirs, files in os.walk('./pdf'):
        for file in files:

            command = "./extract.sh pdf/" + str(file)
            val = subprocess.check_call(command, shell=True)




            subprocess.call("./stai1.py", shell=True)
            subprocess.call("./stai2.py", shell=True)




    time.sleep(1)
