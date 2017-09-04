# prog_challenge

## Synopsis
Simple implementation of a TCP server that accepts client connections and looks up register data using the provided aor and a simple client that connects to the server and queries the server. The server is implemented in the aor_lookup.py file and the client is in client.py. The server has a logfile named aor_lookup.log. 

## Installation

requires Python 2.7

git clone https://github.com/wallnutmonkeys/prog_challenge.git
cd prog_challenge
./aor_lookup.py

## Tests
The client performs 4 tests:
1. queries the server with an AOR that has 2 registers
2. queries the server with an AOR that has 1 register
3. queries the server with a bogus AOR
4. waits 15 seconds before querying the server again in order to trigger the connection timeout
