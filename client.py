#!/usr/bin/env python

"""
A simple network socket client for the base network protocol for B.O.B.
if used in the command line, the argument item will be transmitted to the server
if used as a module in a pythong gui, use import client, and client.send(your text here)
"""

import socket
import sys


if (len(sys.argv) > 1):#looks for a filename to open in the argument line
    text = sys.argv[1]
    host = 'localhost'
    port = 5000
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(text)
    s.close()
else:
    pass

def send(text):
    host = 'localhost'
    port = 5000
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(text)
    s.close()