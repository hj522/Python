# 홀/짝을 입력하시오 홀
# 나: 홀
# 컴: ? (랜덤)
# 결과: 승리/패배
from random import random

na = input("홀/짝을 입력하시오. ")
com = "" #초기화
result = ""

rnd = random()

if rnd > 0.5 :
    com = "홀"
else :
    com = "짝"
    
if com == na :
    result = "승리"
else :
    result = "패배"

print("na",na)
print("com",com)
print("result",result)