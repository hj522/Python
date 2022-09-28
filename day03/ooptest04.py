class Biden:
    def __init__(self):
        self.ac = 10 # 항공모함 개수
    
    def makewar(self):
        self.ac -= 1 # 전쟁할 때마다 1대씩 감소

class Putin:
    def __init__(self):
        self.nuclear = 6660
    def altzheimer(self):
        self.nuclear -= 1
        
class Mugun(Biden, Putin):
    def __init__(self):
       # super().__init__() # super는 단일 상속에서만 사용
        Biden.__init__(self) # 다중 상속
        Putin.__init__(self) # 다중 상속
        

mg = Mugun()

print(mg.ac)
print(mg.nuclear)

mg.makewar()
mg.altzheimer()
print(mg.ac)
print(mg.nuclear)