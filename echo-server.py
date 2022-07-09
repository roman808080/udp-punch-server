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

clients = {}


def convert_client_address_to_bytes(client_address):
    return str(client_address[0]).encode() + b':' + str(client_address[1]).encode()


def create_another_client_message(client_address):
    return b's:connect:' + convert_client_address_to_bytes(client_address)


while True:
    client_id, client_address = sock.recvfrom(1000)
    print("Client address: ", str(client_address), ". Client id: ", client_id)

    clients[client_id] = client_address

    if len(clients) == 2:

        max_amount_of_iterations = 5
        for _ in range(max_amount_of_iterations):
            send_to_second_client = create_another_client_message(clients[b'1'])
            sent = sock.sendto(send_to_second_client, clients[b'2'])
            print("Sent to the second client(" + str(clients[b'2']) + ") information about the first: ", str(send_to_second_client), flush=True)

            send_to_first_client = create_another_client_message(clients[b'2'])
            sent = sock.sendto(send_to_first_client, clients[b'1'])
            print("Sent to the first client(" + str(clients[b'1']) + ") information about the second: ", str(send_to_first_client), flush=True)

            time.sleep(0.5)

        clients.clear()

    else:
        sent = sock.sendto(b's:wait', client_address)
        print("Sent results: ", str(sent), flush=True)
