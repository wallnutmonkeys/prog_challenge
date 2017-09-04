#!bin/python

import socket
import sys
import time


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

    sock.sendall("01577bc1415ed95760000100620002\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response
    time.sleep(3)

    sock.sendall("0148c1f489badb837d000100620002\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response
    time.sleep(5)

    sock.sendall("01576e593243534655555555620007\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response
    time.sleep(15)

    sock.sendall("34534503948503498503495\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response

