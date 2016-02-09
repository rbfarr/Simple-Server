#!/usr/bin/env python

# Richard Farr (rfarr6)
# CS 3251
# 9/21/2014
# Project 1

import socket, sys

# Open TCP socket and bind to localhost on the specified port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", int(sys.argv[1])))

# Listen for a maximum of 1 connection
sock.listen(1)

# Set buffer size to hold received data
buffer_size = 32

while True:

    # Accept incoming TCP connections
    conn, addr = sock.accept()

    # Receive data from client 
    data = conn.recv(buffer_size)

    # Respond to client query
    if (data == "kill"): break

    op, num1, num2 = data.split(" ")

    if (op == "multiply"):
        conn.send(str(int(num1)*int(num2))+"\n")
    elif (op == "add"):
        conn.send(str(int(num1)+int(num2))+"\n")
    else:
        conn.send("invalid operation\n")

# Close connection
conn.close()

