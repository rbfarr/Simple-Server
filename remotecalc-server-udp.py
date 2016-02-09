#!/usr/bin/env python

# Richard Farr (rfarr6)
# CS 3251
# 9/21/2014
# Project 1

import socket, sys

# Bind to 127.0.0.1 at the specified port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", int(sys.argv[1])))

# Buffer size for received data
buffer_size = 32

while True:

    # Receive data and sender's address
    data, addr = sock.recvfrom(buffer_size)

    # Respond to client query
    if (data == "kill"): break

    op, num1, num2 = data.split(" ")

    if (op == "multiply"):
        sock.sendto(str(int(num1)*int(num2))+"\n", addr)
    elif (op == "add"):
        sock.sendto(str(int(num1)+int(num2))+"\n", addr)
    else:
        sock.sendto("invalid operation\n", addr)

# Release bound network interface
sock.close()
