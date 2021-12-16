import time
import logging
import threading
from socketserver import TCPServer, StreamRequestHandler
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class RequestHandler(StreamRequestHandler):

    def __init__(self, request, client_address, server):
        super(RequestHandler, self).__init__(request, client_address, server)

    def handle(self):
        content = self.request.recv(4096)
        logging.debug(content.decode("utf-8"))


def tcp_server():
    server = TCPServer(server_address=("0.0.0.0", 4000),
                       RequestHandlerClass=RequestHandler)
    server.serve_forever()


def main():
    thread = threading.Thread(target=tcp_server, args=())
    thread.daemon = True
    thread.start()

    count = 0
    while count < 600:
        time.sleep(1)
        count += 1


if __name__ == '__main__':
    main()
