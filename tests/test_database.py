from unittest import TestCase
from src.db import DB
import datetime


class TestDatabase(TestCase):

    def setUp(self):
        self.db = DB()

    def test_connection(self):
        connection = self.db.connect()
        self.assertIsNotNone(connection)


    def test_setup(self):
        self.assertEqual(self.db.setup(),None)

    def test_seed(self):
       self.db.connect()
       self.db.setup()
       self.db.seed()
       self.assertIsNone(self.db.seed())

    def test_pages(self):
       self.db.connect()
       self.db.setup()
       self.db.seed()
       selecter=self.db.pages().select()
       self.assertIsNotNone(selecter)
    
    def test_link(self):
       self.db.connect()
       self.db.setup()
       select_link=self.db.links().select()
       self.assertIsNotNone(select_link)
       self.assertEqual(select_link, [])


       