from threading import Thread

class ClientThread(Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        try:
            name = self.conn.recv(1024).decode()
            print(name)
            self.conn.send(bytes(name, 'UTF-8'))
        except Exception as e:
            print(e)
