# Team Members - Derrick Li and Jake Hosking
# Github Repository link: https://github.com/lishouyi1024/usc-ee250-fall2022-project-jake-derrick/tree/main

import socket
from picamera import PiCamera
import time
from fileinput import close
import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
# Bind the socket to the port
server_address = ('192.168.43.75', 8080)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:


    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    numPhotos = 0
    interval = 0

    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024)
            if data.decode() == "delete":
                # delete photos
                for i in range (1, numPhotos+1):
                    os.system("rm buffer" + str(i) + ".jpg")
                connection.close()
                sock.close()
                break  

            # print('received "%s"' % data)
            
            # get parameters from the data 
            tempList = data.decode().split(',')
            numPhotos = int(tempList[0])
            interval = int(tempList[1])

            # take photos

            # camara initialization
            camera = PiCamera()
            camera.start_preview()
            time.sleep(2)
            
            for i in range(1, numPhotos+1):
                camera.capture("buffer" + str(i) + ".jpg")
                if (i + 1 < numPhotos):
                    time.sleep(interval)

            connection.send("Done".encode())

    finally:
        # Clean up the connection
        connection.close()
        sock.close()
