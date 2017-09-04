#!bin/python

import socket
import sys
import time

SERVER_IP = 'localhost'

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
    sock.connect((SERVER_IP, 5000))

    # this aor has 2 registers
    sock.sendall("7tq72ZFDLfSmhsfkmTzyaDbC27YNeP\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response

    # this aor has 1 register
    sock.sendall("0148c1f489badb837d000100620002\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response

    # this is a bogus aor
    sock.sendall("01576e593243534655555555620007\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response
    time.sleep(15)

    # server will close the connection before this gets executed
    sock.sendall("34534503948503498503495\n")
    srv_response = receive_response(sock)
    print "received %s back from server" % srv_response

