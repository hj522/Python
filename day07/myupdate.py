import pymysql

e_id = "3"
e_name = "5"
e_sex = "5"
e_addr = "5"

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       port=3305,
                       db='python',
                       charset='utf8')

#curs=커서.. 자바의 statement급
curs = conn.cursor()

query = f"""
        UPDATE emp
        SET
            e_name = '{e_name}', 
            e_sex = '{e_sex}', 
            e_addr = '{e_addr}' 
        WHERE e_id = '{e_id}'
        """

curs.execute(query)
print("cnt", curs.rowcount)

conn.commit()
curs.close()
conn.close()
