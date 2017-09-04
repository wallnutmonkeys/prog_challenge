#!bin/python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)

sock.bind(server_address)

sock.listen(1)

while True:
    print "waiting for a connection"
    connection, client_address = sock.accept()
    try:
        print "connection from", client_address
       
        rcv_buff = ''

        while True:
            data = connection.recv(1)
            if data != '\n':
                rcv_buff += data
            else:
                print "received: %s" % (rcv_buff,)
                response = "blablablablabla"
                print "sending back %s" % response
                connection.sendall(response + "\n")
                rcv_buff = ''

    finally:
        connection.close()



