import datetime
import requests
import sqlite3


# @author lxy
# UtilClass for dag

class dagutil:
    '''
    generate a seq number for a dag run
    @:param taskid: a unique task id represents the task about to run
    '''

    def getseqnum(taskid):
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y%m%d%H%M%S")
        seq = str(taskid) + otherStyleTime
        return seq

    '''
    to trigger the run
    @:param taskid: a unique task id represents the task about to run
    '''

    def do_post(url, payload):
        # payload = {'key1': taskid, 'key2': 'value2'}
        r = requests.post(url, data=payload)
        print(r.text)
        return True

    def parse_get_result(response):
        result = response.content.decode("UTF-8")
        return True if "True" in result else False

    def getrunid():
        conn = sqlite3.connect('/home/bluescv/airflow/airflow.db')
        cursor = conn.cursor()
        # select dag run id from the table dag_run
        cursor.execute("select run_id from dag_run where dag_id=?", ('httpdag',))

        for row in cursor:
            print(row[0])

        cursor.close()
        conn.close()


if __name__ == '__main__':

    try:
        print(dagutil.getseqnum("id"))

    except KeyboardInterrupt:
        print("exception")

    pass
