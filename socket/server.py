
import socket
def server():
    ##creat a socket
    s = socket.socket()
    host = "127.0.0.1"
    port = 6665
    s.bind((host,port))
    #
    s.listen(10)
    while True:
        # Return a new socket
        #representing the connection, and the address of the client.
        c,addr = s.accept()
        print('Connect Address : ' , addr)
        c.send(b'Welcome to our course')
        c.close()



server()
