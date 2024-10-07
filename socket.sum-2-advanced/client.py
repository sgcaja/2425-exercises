#!/usr/bin/python3
import socket
import struct
import sys #Esta libreria permite interactuar con el entorno

if len(sys.argv) < 2: #Se comprueba los argumentos (Si los argumentos son menor que 2)
    print(f"Usage: {sys.argv[0]} <server_host> <number_1> <number_2> ... <number_n>") #Imprime el mensaje
    sys.exit(1) #Se termina el programa 

ip = sys.argv[1] #De los argumentos, el primero es la IP
numbers = [int(x) for x in sys.argv[2:]] #Numbers es una lista, se itera sobre todos los numeros que se pasan desde el argv 2 y se convierte a int

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #Se crea el socket IPV4 tipo UDP
    data_format = "!" + "h" * len(numbers) #Se establece formato, longitud de la lista de numbers

    print(f"Message format is: {data_format}") #Demuestra el formato

#   SE EMPAQUETA
    data = struct.pack(data_format, *numbers) #Empaqueta la informacion, especificando el formato !hh * descompone la lista, en vez de pasar [3, 4] pasa 3, 4
    
    s.sendto(data, (ip, 1234)) #Envia al servidor los datos empaquetados, se indica la ip y el puerto

    data = s.recv(1024) #Recibe un mensaje del servidor tam 1024 y lo almacena en 'data', este mensaje esta en bYTES (empaquetado)
    result = struct.unpack("!i", data)[0] #Se desempaqueta el mensaje, devuelve una tupla, pero como solo se espera un valor (el resultado), se accede al primer (y único) elemento con [0].

    print(f"Result: {result}") #Imprime resultado 
