#!/usr/bin/env

import socket
import sys
import json
from registers import Registers
import logging

REGISTRATION_FILEPATH = './registrations.json'
PORT = 5000
CONNECTION_TIMEOUT = 10.0


if __name__ == "__main__":

    logging.basicConfig(filename='aor_lookup.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')
    logging.info("starting up the server")

    registers = Registers()
    registers.from_file(REGISTRATION_FILEPATH)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', PORT)
    sock.bind(server_address)
    sock.listen(1)
    logging.info("listening on port %d" % PORT)

    while True:
        print "waiting for a connection"
        connection, client_address = sock.accept()
        connection.settimeout(CONNECTION_TIMEOUT)
        try:
            logging.info("accepting connection from %s" % str(client_address))
       
            rcv_buff = ''

            while True:
                data = connection.recv(1)
                if data != '\n':
                    rcv_buff += data
                else:
                    aor = rcv_buff
                    logging.info("received a lookup request for aor: %s from client %s" % (aor, str(client_address)))
                    ret = ''
                    try:
                        ret = registers.lookup(aor)
                        logging.info("found matching register(s) for aor: %s" % aor)
                    except KeyError:
                        logging.info("no match found for aor: %s" % aor)

                    logging.info("sending back: %s to %s" % (ret,str(client_address)))
                    connection.sendall(ret + "\n")

                    rcv_buff = ''

        except socket.timeout:
            logging.warning("connection to %s has timed out" % str(client_address))

        finally:
            logging.info("closing connection to %s" % str(client_address))
            connection.close()



