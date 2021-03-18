#!/usr/bin/env python3

import subprocess, os, sys

def load_model():
    for root, dirs, files in os.walk(os.getcwd()):
        if len(files) == 0:
            print("No files found.")
            sys.exit()
        
        print ("Select a model:\n")

        i = 1
        for file in files:
            print(str(i) + ")", file)
            i += 1
                  
        inp = int(input("\nChoice: ")) - 1
        if inp >= len(files):
            print("Wrong input.")
            input()
            sys.exit()

        return files[inp]
        
f_name = load_model()
print(f_name)
test = subprocess.Popen(["sudo",  "chmod", "u+x", f_name], stdout=subprocess.PIPE)
output = test.communicate()[0]

input("Press Enter to exit: ")
