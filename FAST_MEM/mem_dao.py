import pymysql

# member CRUD
class MemDao:
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       port=3305,
                       db='python',
                       charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)    #self가 붙으면 전역 변수
    
    def selects(self):
        sql = "SELECT m_seq,m_name,m_tel,army_yn FROM member"    # '*'은 쓰지 않는 것이 좋다!
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows

    def select(self,m_seq):
        sql = f"""
            SELECT
                m_seq,
                m_name,
                m_tel,
                army_yn
            FROM
                member
            WHERE
                m_seq = '{m_seq}'
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows[0]
    #   return None # null과 같은 개념
    
    def insert(self,m_name,m_tel,army_yn):
        sql = f"""
            INSERT INTO member
            (m_name,m_tel,army_yn)
            VALUES
            ('{m_name}','{m_tel}','{army_yn}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,m_seq,m_name,m_tel,army_yn):
        sql = f"""
            UPDATE member
            SET
                m_name = '{m_name}', 
                m_tel = '{m_tel}', 
                army_yn = '{army_yn}' 
            WHERE
                m_seq = '{m_seq}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,m_seq):
        sql = f"""
            DELETE FROM member
            WHERE
                m_seq = '{m_seq}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
        #소멸자
    def __del__(self):
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    md = MemDao()
    cnt = md.delete('3')
    print(cnt)