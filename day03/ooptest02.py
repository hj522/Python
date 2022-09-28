class Car :
    
        # 생성자
    def __init__(self):
        self.speed = 0
        print("생성",self.speed)
        
    def accel(self, strength):
        self.speed += strength
        
        # 소멸자
        # java에서는 가비지컬렉터때문에 없음
    def __del__(self):
        self.speed = 0
        print("소멸",self.speed)

if __name__ == '__main__': # main을 사용하면 test03에서 실행되지 않음
    c = Car()
    print(c.speed)
    c.accel(100)
    print(c.speed)