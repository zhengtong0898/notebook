import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 4000))
sock.sendall(b"helloworld\n")
sock.sendall(b"good good study.1\n")
sock.sendall(b"good good study.2\n")

sock.close()
