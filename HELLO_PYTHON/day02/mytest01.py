# 첫 수를 넣으세요 2
# 끝 수를 넣으세요 4
# 2에서 4까지의 합은 9입니다

a = input("첫 수를 넣으세요 ")
b = input("끝 수를 넣으세요 ")

aa = int(a)
bb = int(b)

total = 0
for c in range(aa,bb+1) :
    total += c
    
# print(aa,"에서",bb,"까지의 합은",total,"입니다.")
print("{}에서 {}까지의 합은 {}입니다.".format(aa,bb,total))