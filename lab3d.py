#!/usr/bin/env python3

# Author ID: 158174227

import subprocess

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    final = output[0].decode('utf-8').strip()
    return final

print(free_space())
