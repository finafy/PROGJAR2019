import socket


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    print "Instruksi :"
    print "1. masukkan nama file untuk download file pada directory ini"
    print "2. masukkan folder/namafile untuk melakukan download file dari folder kedalam new_folder"
    print " "

    filename = raw_input("Filename? -> ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File tersedia, " + str(filesize) + "Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open('new_' + filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done"
                print "Download Selesai!"
                f.close()
        else:
            print "File tidak tersedia!"

    s.close()


if __name__ == '__main__':
    Main()