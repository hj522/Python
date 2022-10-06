import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       port=3305,
                       db='python',
                       charset='utf8')

#curs=커서.. 자바의 statement급
curs = conn.cursor()

query = """DELETE FROM emp WHERE e_id = %s"""

curs.execute(query, 3) #id가 3인 것
print("cnt", curs.rowcount)

conn.commit()
curs.close()
conn.close()

