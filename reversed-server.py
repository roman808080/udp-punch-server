#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: David Manouchehri <manouchehri@protonmail.com>
# This script will always echo back data on the UDP port of your choice.
# Useful if you want nmap to report a UDP port as "open" instead of "open|filtered" on a standard scan.
# Works with both Python 2 & 3.

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 31337

server = (server_address, server_port)
sock.bind(server)
print("Listening on ", server_address, ":", str(server_port), flush=True)

message, client_address = sock.recvfrom(1000)
print("Client address: ", str(client_address), ". Client message: ", message)
sock.close()

time.sleep(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    sent = sock.sendto(b'Now I am a client(((', client_address)
    print("Sent a message to a client which is now a server: ", client_address)

    message, client_address = sock.recvfrom(1000)
    print("Our new lord answers: ", message)

    time.sleep(1)
