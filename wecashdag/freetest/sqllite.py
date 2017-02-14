import sqlite3

conn = sqlite3.connect('/home/bluescv/airflow/airflow.db')
cursor = conn.cursor()
# obtain the table structure
cursor.execute('select * from sqlite_master WHERE type =?', ('table',))
# select dag run id from the table dag_run
cursor.execute("select run_id from dag_run where dag_id=?", ('httpdag',))

# values = cursor.fetchall()
# for value in values:
#     print(value)

for row in cursor:
    print(row[0])

cursor.close()
conn.close()
