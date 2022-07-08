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

while True:
    payload, client_address = sock.recvfrom(1000)
    print("Echoing data back to ", str(client_address), ": ", payload)
    response = bytes(client_address[0], 'utf-8') + b':' + str(client_address[1]).encode()
    sent = sock.sendto(response, client_address)
    print("Sent results: ", str(sent), flush=True)

