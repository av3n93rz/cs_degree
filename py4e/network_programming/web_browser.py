import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

data = None

while True:
    packet = mysock.recv(512)
    if len(packet) < 1:
        break
    if data is None:
        data = packet
    else:
        data = data + packet
    
    
mysock.close()

""" print(data.decode()) """

res = re.findall('\r\n\r\n([\d\D]*$)', data.decode())
if len(res) > 0:
    print(res[0])

