#!/usr/bin/env python3

import sys

# Author: Anthony JAyaratnam
# Author ID: ajjayaratnam
# Date Created: 2024/09/24

# This script uses a command-line argument as the starting value for a countdown

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} timer_value")
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
