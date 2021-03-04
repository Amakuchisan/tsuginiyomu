import logging

from server import server

if __name__ == '__main__':
    logging.basicConfig()
    server.serve()
