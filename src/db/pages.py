class Pages:
  '''This provides implementations for querying the pages table in the database'''
  
  def __init__(self,connect):
    self.conn= connect
    self.cursor = connect.cursor()

  def insert(self, content):
    self.conn.execute('INSERT INTO pages  (url)', content)
    self.conn.commit()

  
  def select(self):
    self.cursor.execute('SELECT * FROM pages')
    record = self.cursor.fetchall()
    return record
    

  def find(self, id):

    self.cursor.execute('SELECT * FROM pages Where id =%s', (id,))
    record = self.cursor.fetchone()
    return record
    

  def update(self, id, is_scraping):
    self.cursor.execute('''UPDATE pages 
        SET is_scraping=%s
        Where id =%s''', (is_scraping, id))

    self.conn.commit()
    

  def delete(self, id):
    self.cursor.execute('DELETE FROM links Where id=%s', (id,))
    self.conn.commit()
  