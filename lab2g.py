#!/usr/bin/env python3

import sys

# Author: Anthony Jayaratnam
# Author ID: ajjayaratnam
# Date Created: 2024/09/24

# This script checks for a command-line argument; defaults to 3 if none provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
