import socket
import threading


class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.pool = threading.Thread(target=self._server)
        self.pool.start()

    def _server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.host, self.port))
        client = []
        print('Start Server')

        while True:
            data, address = sock.recvfrom(1024)
            print(address[0], address[1])
            if address not in client:
                client.append(address)
                print(client)
            for clients in client:
                if clients == address:
                    continue
                sock.sendto(data, clients)
                print(data, clients)


host = '127.0.0.1'
port = 9090
server = Server(host=host, port=port)