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

# Bind to input ip and port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket timeout
sock.settimeout(2.0)

while True:

    # Send packet
    sock.sendto(query, (dest_ip, int(dest_port)))

    # Attempt to receive packet and print reponse. Timeout will raise an exception.

    try:
        data, addr = sock.recvfrom(buffer_size)
        print "From server:", data
        break
    except socket.timeout:
        print "The server has not answered in 2 seconds."
        print "Enter 'retry' to resend the message or 'exit' to exit the application:"

        resp = sys.stdin.readline()[:-1]

        if resp != "retry": break

