import pymysql
import os

host = os.environ.get("host", "localhost")
port = os.environ.get("port", 3306)
user = os.environ.get("user", "root")
password = os.environ.get("password", "root")

if __name__ == '__main__':
    conn = pymysql.connect(host=host, port=int(port), user=user, password=password)
    cursor = conn.cursor()
    cursor.execute('show databases')
    print(cursor.fetchall())
    