#!/usr/bin/env python

# Richard Farr (rfarr6)
# CS 3251
# 9/21/2014
# Project 1

import socket, sys

# Parse input ip and port
dest_ip, dest_port = sys.argv[1].split(":")

# Construct query
query = " ".join(sys.argv[2:])

# Set buffer size for server response
buffer_size = 32

# Create TCP socket and bind to specified ip and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server

try:
    sock.connect((dest_ip, int(dest_port)))
except socket.error:
    print "unable to connect to server"
    sys.exit()

# Send query
sock.send(query)

# Receive server response
data = sock.recv(buffer_size)

# Close TCP connection
sock.close()

print "From server:", data
