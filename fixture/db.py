# -*- coding: utf-8 -*-
import psycopg2
from model.base import Base


class DbFixture:

    def __init__(self, database, username, password, host, port):
        self.database = database
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
        self.connection.autocommit = True

    def get_group_list(self):
        list_app = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, amount, username from automation")
            for row in cursor.fetchall():
                (id, amount, username) = row
                list_app.append(Base(id=id, amount=amount, username=str(username)))
        finally:
            cursor.close()
        return list_app

    def destroy(self):
        self.connection.close()
