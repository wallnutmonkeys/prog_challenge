#!bin/python

import socket
import sys
import json

def load_json(json_filepath):
    registers = []
    with open(json_filepath,'r') as reg_file:
        for line in reg_file:
            registers.append(json.loads(line.strip()))
    return registers

def lookup_aor(registers,aor):
    for r in registers:
        if r['addressOfRecord'] == aor:
            return r
    return None

if __name__ == "__main__":

    registers = load_json('./registrations.json')
    
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print "waiting for a connection"
        connection, client_address = sock.accept()
        connection.settimeout(10.0)
        try:
            print "connection from", client_address
       
            rcv_buff = ''

            while True:
                data = connection.recv(1)
                if data != '\n':
                    rcv_buff += data
                else:
                    aor = rcv_buff
                    print "looking up aor: %s" % aor
                    register = lookup_aor(registers, aor)
                    if not register:
                        print "register with aor:'%s' not found" % aor
                    else:
                        print "register with aor:'%s' was found" % aor
                        connection.sendall(json.dumps(register) + "\n")
                    rcv_buff = ''
        except socket.timeout:
            print "timeout"

        finally:
            connection.close()



