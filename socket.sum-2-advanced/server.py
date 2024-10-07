#!/usr/bin/python3
import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 1234)) #Recibe todas las direcciones del puerto 1234

    while 1:
        data, client = s.recvfrom(1024) #Esto es una tupla, devuelve (data y addr) (mensaje y direccion del cliente) addr a su misma vez es una tupla(ip, puerto)
        data_format = "!" + "h"* (len(data) // 2) #Calcula la longitud del mensaje empaquetado en bytes, como se sabe que es de h (2bytes) se saca la longitud y se divide en 2 para sacar la cantidad de enteros que hay
     
        #Tambien se puede utilizar          "!{}.H".format(len(data)//2) pero me es mas dificil de memorizar y entender. Aqui daria lo mismo pero en formato !4h que es lo mismo que !hhhh
        print(f"Message format is: {data_format}")

#SE DESEMPAQUETA
        numbers = struct.unpack(data_format, data) #desempaqueta y los guarda en una lista
        result = sum(numbers) #se suaman

        print(f"{client} :: result = {result}")
#SE EMPAQUETA
        s.sendto(struct.pack("!i", result), client) #se devuelve al cliente
