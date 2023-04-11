import MySQLdb
import os

host = os.environ.get("host", "localhost")
port = os.environ.get("port", 3306)
db = os.environ.get("database", "temp")
user = os.environ.get("user", "root")
password = os.environ.get("password", "root")

if __name__ == '__main__':
    conn = MySQLdb.connect(host = host, port = port, user = user, db = db, password = password)
    cur = conn.cursor()

    cur.execute('select * from wp_posts')
    for i in range(cur.rowcount):
        row = cur.fetchone()
        print(row)

    cur.close()

    conn.close()
