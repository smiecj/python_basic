from pyhive import hive
from TCLIService.ttypes import TOperationState

cursor = hive.connect(host='hive_server_host', username='user_name').cursor()
cursor.execute('SELECT COUNT(*) FROM table_name LIMIT 10')

status = cursor.poll().operationState
while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
    logs = cursor.fetch_logs()
    for message in logs:
        print(message)

    status = cursor.poll().operationState

print(cursor.fetchall())