import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       port=3305,
                       db='python',
                       charset='utf8')

#curs=커서.. 자바의 statement급
curs = conn.cursor()

query = """INSERT INTO emp (e_id, e_name, e_sex, e_addr) VALUES (%s, %s, %s, %s)"""

cnt = curs.execute(query, ('3', '3', '3', '3'))
print("cnt", curs.rowcount)

conn.commit()
curs.close()
conn.close()

