import psycopg2
from config import config

class Banco():
    def __init__(self):
        self.conn = None
        self.params = config()
        self.conn = psycopg2.connect(**params)
        self.cur = conn.cursor()

