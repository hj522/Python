# 멀티 리턴
# return 개수가 같을 때 or 1개일 때 출력 가능

def addminmuldiv(a,b):
    return a+b, a-b, a*b, a/b

#sum,min,mul,div= addminmuldiv(4,6)

# 멀티 리턴을 한 번에 담아주는 튜플
sum = addminmuldiv(4,6)
print("sum",sum)

#print("+",sum)
#print("-",min)
#print("*",mul)
#print("/",div)