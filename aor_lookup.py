#!bin/python

import socket
import sys
import json
from registers import Registers


if __name__ == "__main__":

    registers = Registers()
    registers.from_file('registrations.json')
    print registers
    exit(1)
    
    
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



