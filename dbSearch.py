#!/usr/bin/env python3

# dbSearch made by shinigami
# Github: https://github.com/inheritably

import sys

db = sys.argv[1]
string = sys.argv[2]
with open(f"{db}") as f:
    lines = f.readlines()
    for line in lines:
        if string in line:
            print(line)
