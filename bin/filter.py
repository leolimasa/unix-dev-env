#!/usr/bin/env python3

import fileinput

def get_stdin():
    return ''.join([line for line in fileinput.input()])

print(get_stdin())
    
