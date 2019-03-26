from threading import Thread
import socket
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000
FILE_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
server_addrssess = (SERVER_IP, SERVER_PORT)
sock.bind(server_addrssess)

namanama = ["doraemon.jpg", "nobita.jpg", "shizuka.jpg"]

def sendImage(CLIENT_IP, CLIENT_PORT):
	addrss = (CLIENT_IP, CLIENT_PORT)
	sock.sendto("START", (addrss))
	for nama in namanama:
		image_size = os.stat(nama).st_size
		sock.sendto("SEND {}" .format(nama), (addrss))
		fp = open(nama,'rb')
		read = fp.read()
		size = 0
		for x in read:
			sock.sendto(x, (addrss))
			size = size + 1
   			print "\r sent {} of {} " . format(size ,image_size)
   		sock.sendto("DONE", (addrss))
   		fp.close()

   	sock.sendto("END", (addrss))

while True:
	print "Waiting..."
	data, addrss = sock.recvfrom(1024)
	print "Receiving: " + str(data)
	if str(data) == "READY":
		thread = Thread(target=sendImage, args=(addrss))
		thread.start()
