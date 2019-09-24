import binascii
from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('172.16.127.233', 27019))
msg = b'hello'
# print(msg.decode('utf-8'))
s.send(msg)
# print(binascii.b2a_hex(msg))
print(s.recv(1024))