# 첫 수를 넣으세요 2
# 끝 수를 넣으세요 4
# 배수를 넣으세요 3
# 2에서 4까지 3의 배수의 합은 3입니다.

first = input("첫 수를 넣으세요 ")
second = input("끝 수를 넣으세요 ")
third = input("배수를 넣으세요 ")

a = int(first)
b = int(second)
c = int(third)

total = 0

for d in range(a,b+1) :
    if(d % c == 0) :
        total += d

print("total",total)
print("{}에서 {}까지 {}의 배수의 합은 {}입니다.".format(a,b,c,total))
