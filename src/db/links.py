
class Links:
  '''This provides implementations for querying the links table in the database'''

  def __init__(self,connect):
    self.conn= connect
    self.cursor=self.conn.cursor()

  def insert(self,page_id, url):
    self.cursor.execute('''INSERT INTO links (page_id, url)
    VALUES (%s, %s)''', (page_id,url))
    self.conn.commit()

  def select(self):
    self.cursor.execute('SELECT * FROM links')
    record = self.cursor.fetchall()
    return record
    

  def find(self, id):
   
    self.cursor.execute('SELECT * FROM links Where id =%s', (id,))
    record = self.cursor.fetchone()
    return record
    

  def update(self, id, is_scraping):
    self.cursor.execute('''UPDATE links 
        SET is_scraping =%s
        Where id =%s''', (is_scraping, id))

    self.conn.commit()
    

  def delete(self, page_id):
    self.cursor.execute('DELETE FROM links Where page_id=%s', (page_id,))
    self.conn.commit()

