
"""
작성자 : 김문희
기능 : 리스트 자료형 연습, 제어문
작성일 : 2020-01-17
"""


#실습 1
a = [90,90,80]    #1
b = [70,80,90]
c = [24,35,100]
a.append(a[0]+a[1]+a[2])
b.append(b[0]+b[1]+b[2])
c.append(c[0]+c[1]+c[2])
print(a[3] + b[3] + c[3])


number = [1,2,3,4,5,6,7,8,9,10] #2
number.sort()
print(number[0], number[-1])

#실습 2
score = [[20170101,'홍길동',90],[20172831,'성춘향',95],[20172831,'이몽룡',85]]
score.sort()
print(score[0][0],score[0][1],score[0][2]),print(score[1][0],score[1][1],score[1][2])\
        ,print(score[2][0],score[2][1],score[2][2])
"""제어문"""
#실습 1

a = int(input("숫자?"))
if a%2 == 0:
    print(a,"은 짝수")
else:
    print(a,"은 홀수")

a = int(input("숫자?"))
if a%2 == 0 and a%3 ==0:
    print("6의 배수")

a = int(input("숫자?"))
if a%2 != 0 or a%3==0:
    print("홀홀")

#실습 2

menu = ['햄버거','돈가스','삼겹살']
order = str(input('메뉴를 입력하세요'))
if order in menu :
    print('판매합니다')
else:
    print('안팔아요')
#실습 3
a = int(input("년도는?"))
if a%4 == 0:
    if a%100 == 0:
        if a%400 == 0:
            print("윤년입니다.")
        else:
            print("윤년이 아닙니다.")
    else:
        print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
    


# 실습 4
sum = 0
for i in list(range(1,101)):
    if i%2==0:
        sum = sum + i
print(sum)

#실습 5
for i in range(1,7):
	for j in range(1,i):
		print("", end=" ")
	print("*")


# 과제
#1
def guessing():
	import random
	round = 0
	my_number = random.randint(1,20)
	while True:
		round = round + 1
		n = int(input("내가 생각한 숫자를 맞추세요"))
		if n == my_number:
			print(round,"회만에 맞았습니다.",my_number,"에요")
			break
		elif n > my_number:
			print("숫자가 커요. 작은 숫자를 다시 넣으세요")
		else:
			print("숫자가 작아요. 큰 숫자를 다시 넣으세요")

#2

for i in range(1,7):
	for j in range(1,i):
		print(" ", end="")
	print("*")

#3
for i in range(2,10):
    for j in range(2,10):
        print(i,"*",j,"=",i*j)

#4
number = []
for i in range(1,101):
    number.append(3*i)

#5
def bmi_calculator():
	h = float(input("당신의 키는(cm)?"))
	w = float(input("당신의 몸무게는?"))
	bmi = w/((h/100)*(h/100))
	print("당신의 BMI 지수는",bmi)
	if bmi <= 18.5:
		print("저체중입니다.")
	elif bmi > 18.5 and bmi <= 23 :
		print("정상입니다.")
	elif bmi >23 and bmi <=25:
		print("과체중입니다.")
	elif bmi > 25 and bmi <= 30:
		print("비만입니다.")
	elif bmi > 30 and bmi <=35 :
		print("고도비만입니다.")
	else:
		print("초고도비만입니다.")
