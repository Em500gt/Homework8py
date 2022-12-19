import sqlite3

def init_base():
   conn = sqlite3.connect('base.db')

   cur = conn.cursor()

   cur.execute("""CREATE TABLE IF NOT EXISTS users (
      name TEXT,
      pass TEXT,
      status TEXT);
   """)

   conn.commit()

   cur.execute("""CREATE TABLE IF NOT EXISTS time_table (
      lesson TEXT,
      home TEXT
      );
   """)

   conn.close()