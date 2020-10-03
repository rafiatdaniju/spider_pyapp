from psycopg2 import connect, sql
from decouple import config
from .links import Links
from .pages import Pages
import textwrap


class DB:
    @classmethod
    def connect(cls):
        try:
            conn = connect(
                dbname=config('DB_NAME'),
                user=config('DB_USER'),
                password=config('DB_PASSWORD'),
                host=config('DB_HOST'),
                port=config('DB_PORT', cast=int))
            cursor = conn.cursor()
        except Exception as error:
            print(f'Can not connect to database: {error}')

        conn.autocommit = True
        return conn

    @classmethod
    def setup(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        with open('src/schemas/structure.sql', 'r') as f_in:
            lines = f_in.read()
            query_string = textwrap.dedent("""{}""".format(lines))
            cursor.execute(sql.SQL(query_string))

    @classmethod
    def seed(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        with open('src/schemas/seed.sql', 'r') as f_in:
            lines = f_in.read()
            query_string = textwrap.dedent("""{}""".format(lines))
            cursor.execute(sql.SQL(query_string))
            conn.commit()

    @classmethod
    def links(cls):
        connection = cls.connect()
        link = Links(connection)
        return link

    @classmethod
    def pages(cls):
        connect = cls.connect()
        page = Pages(connect)
        return page
