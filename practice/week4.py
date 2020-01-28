"""
작성자 : 김문희
작성일자 : 2020-01-26
내용 : 문자열
"""


#실습 1
a = str(input("문장을 입력하세요"))
word_count = a.count(" ") + 1
a = a.replace(" ","\n")
print(a)
print("(총",word_count,"단어)")


    
    
#실습 2
def num():
	number_list = []
	sum = 0
	while True:
		number = int(input("""숫자를 입력하세요.
                                   단, 1부터 10000사이의 정수를 입력하세요"""))
		number_list.append(number)
		for i in number_list:
			print("+ %4d" % i)
			sum = sum + i
		print("= %4d" %sum)

		
#실습 3
a = str(input("수식을 입력하세요. 단, 덧셈만 가능합니다."))
b = a.split("+")
sum = 0
for i in b :
    sum = sum + int(i)
print("합계는 %d" % sum)
