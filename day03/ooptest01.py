# oop 객체지향프로그래밍 object oriented programming

class Animal:
    
    def __init__(self):
        self.hungry = 5
    
    def timegoby(self):
        if self.hungry > 0 :
            self.hungry -= 1
            
    def manttang(self):
        self.hungry = 10

class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.skill_lang = 5
    
    def momstouch(self, stroke):
        self.skill_lang += stroke

hum = Human()  # new는 생략
print(hum.skill_lang)
print(hum.hungry)

hum.manttang()
hum.momstouch(11)
print(hum.skill_lang)
print(hum.hungry)

#ani = Animal()
#print(ani.hungry)
#ani.timegoby()
#ani.manttang()
#print(ani.hungry)