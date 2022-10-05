import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       port=3305,
                       db='python',
                       charset='utf8')

#curs=커서.. 자바의 statement급
curs = conn.cursor()
query = "SELECT * FROM emp ORDER BY e_id"
curs.execute(query)

rows = curs.fetchall()
print(rows)

conn.close()
curs.close()
