import sys
import socket
from typing import BinaryIO
import struct
buffsize = 256

def stopandwait_server(iface:str, port:int, fp:BinaryIO) -> None:
    print("Hello, I am a server")
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addrs = socket.getaddrinfo(iface, port)
    udp_server.bind(addrs[0][-1])
    while True:
        rcv_d, client = udp_server.recvfrom(264)
        ack, length, msg = struct.unpack('ii256s', rcv_d)
        msg = msg[:length]
        fp.write(msg)
        udp_server.sendto(str(ack).encode(),client)
        if length == 0:
            break

def stopandwait_client(host:str, port:int, fp:BinaryIO) -> None:
    print("Hello, I am a client")
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.connect((host, port))
    forw = False
    set_ack = 0
    while True:
        if not(forw):
            dblck = fp.read(buffsize)
            if not(dblck):
                dblck = b''
        data = struct.pack('ii256s', set_ack, len(dblck), dblck)
        udp_client.send(data)
        try:
            udp_client.settimeout(0.6)
            ackReceived, server = udp_client.recvfrom(buffsize)
            ackReceived = ackReceived.decode()
            if int(ackReceived) == set_ack:
                set_ack = set_ack + 1
                forw = False
        except:
            forw = True

        if not(dblck or forw):
            udp_client.close()
            break