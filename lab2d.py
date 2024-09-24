#!/usr/bin/env python3

import sys

# This script checks if two command-line arguments are given, and prints usage if not

# Check if there are exactly 2 additional arguments (3 in total including script name)
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Exit with code 0 to indicate successful handling of the case

# Assign the arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Print the output message
print(f"Hi {name}, you are {age} years old.")

