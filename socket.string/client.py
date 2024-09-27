#!/usr/bin/python3
import socket
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <server_ip>")
    sys.exit(1)

ip = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    msg = input("Enter message: ") #Se pide al usuario que introduzca un mensaje en cuestion
    
    #SE CODIFICA
    s.sendto(msg.encode(), (ip, 1234)) #se codifica 

    msg, server = s.recvfrom(1024)
    #SE DECODIFICA
    print(f"{server} :: {msg.decode()}")
