from impala.dbapi import connect

conn = connect(host='impalad_host', port=21050, user='user_name', auth_mechanism="NOSASL")
cur = conn.cursor()

cur.execute("SHOW databases")

results = cur.fetchall()
# print(results)

for row in cur:
    print(row)