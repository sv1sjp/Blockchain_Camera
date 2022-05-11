#!/usr/bin/python

"""
Copyright (C) 2022  Dimitris Vagiakakos (sv1sjp)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or any later version. This program 
is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this document. 
 If not, see https://www.gnu.org/licenses/gpl-3.0.html
For any information, find me on: https://sv1sjp.github.io 
or contact me at: dimitrislinuxos@protonmail.ch or @sv1sjp in any social media platform.

"""

import os,subprocess

file= open("../logs/blockchaincamera.log","r").readlines()


for i,line in enumerate(file):
    successes= open("../logs/successes","r")
    
   
    if "hasn't" in line and i>int(successes.readline().strip()):
        print(line)
        
        if os.path.exists("hashes"):
            os.remove("hashes")

        with open("hashes","w") as hashes:
            hashes.write(line[60:188])

        

        successes= open("../logs/successes","w")
        successes.write(str(i))      
        print(i)    

        subprocess.call("python3 send_to_blockchain.py", shell=True)
        
        break

