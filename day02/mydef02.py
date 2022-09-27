# 구구단을 짜시오

#print("{}*{}={}".format(2,1,2*1))
#print("{}*{}={}".format(2,2,2*2))

for i in range(2,9+1) :
    if i % 2 == 0 :
        for j in range(1,9+1) :
            print("{}*{}={}".format(i,j,i*j))
            
print("-------")

# 짝수 단만 출력
for i in range(2,9+1) :
    if i % 2 == 0 :
        for j in range(1,9+1) :
            print("{}*{}={}".format(i,j,i*j))