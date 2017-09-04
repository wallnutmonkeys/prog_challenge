#!bin/python

import socket
import sys


def receive_response(sock):
    rcv_buff = ''
    data = True
    while data:
        data = sock.recv(1)
        if data != '\n':
            rcv_buff += data
        else:
            return rcv_buff

    raise Exception("error reading from server")


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(('localhost', 5000))

    sock.sendall("myaor1\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response

    sock.sendall("myaor2\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response

    sock.sendall("myaor3\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response

    sock.sendall("myaor4\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response
