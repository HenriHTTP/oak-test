import sqlite3


class Databases:
    conn = None
    cur = None

    @classmethod
    def init_connection(cls, db_file):
        cls.conn = sqlite3.connect(db_file)
        cls.cur = cls.conn.cursor()
        cls.conn.commit()

    @classmethod
    def get_connection(cls):
        return cls.conn

    @classmethod
    def get_cursor(cls):
        return cls.cur

    @classmethod
    def close(cls):
        if cls.conn:
            cls.conn.close()