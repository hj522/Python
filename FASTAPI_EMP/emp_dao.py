import pymysql

# emp CRUD
class EmpDao:
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       port=3305,
                       db='python',
                       charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)    #self가 붙으면 전역 변수
    
    def selects(self):
        sql = "SELECT e_id,e_name,e_sex,e_addr FROM emp"    # '*'은 쓰지 않는 것이 좋다!
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows

    def select(self,e_id):
        sql = f"""
            SELECT
                e_id,
                e_name,
                e_sex,
                e_addr
            FROM
                emp
            WHERE
                e_id = '{e_id}'
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows[0]
    #   return None # null과 같은 개념
    
    def insert(self,e_id,e_name,e_sex,e_addr):
        sql = f"""
            INSERT INTO emp
            (e_id,e_name,e_sex,e_addr)
            VALUES
            ('{e_id}','{e_name}','{e_sex}','{e_addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,e_id,e_name,e_sex,e_addr):
        sql = f"""
            UPDATE emp
            SET
                e_name = '{e_name}', 
                e_sex = '{e_sex}', 
                e_addr = '{e_addr}' 
            WHERE
                e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
            DELETE FROM emp
            WHERE
                e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
        #소멸자
    def __del__(self):
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    ed = EmpDao()
    cnt = ed.delete('3')
    print(cnt)