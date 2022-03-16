from pyhive import presto

cursor = presto.connect(host='presto_host',port="presto_port").cursor()
cursor.execute('SELECT * FROM table_name LIMIT 10')
print(cursor.fetchone())
print(cursor.fetchall())