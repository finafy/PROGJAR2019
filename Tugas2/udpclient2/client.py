import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("READY", (SERVER_IP, SERVER_PORT))

def getImage():
	received = 0
	while True:
		data, addr = sock.recvfrom(1024)
		if data[:4] == "SEND":
			print data[5:]
			fp = open(data[5:], "wb+")
		elif data[:6] == "DONE":
			fp.close()
			received = 0
		elif data[:3] == "END":
			print "Selesai"
			break
		else:
			fp.write(data)
			received += len(data)
			print "Menerima " + str(received)
while True:
	data, addr = sock.recvfrom(1024)
	if str(data) == "START":
		print "Manerima data"
		getImage()
		break
