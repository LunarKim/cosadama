"""
작성자 : 김문희
작성일지 : 2020-02-02
내용 : 함수, 파일입출력
"""
#함수
#실습 1

def print_dan(x):
	for i in list(range(1,10)):
		print (x * i)

dan = int(input("숫자를 입력하세요"))
while dan != 0:
	print_dan(dan)
	dan = int(input())

# 실습 2

num = float(input('온도는?, 단 숫자만 입력하라.'))
scale = str(input('섭씨는 c, 화씨는f를 입력하세요')).lower()

def celtofah(x):
	f = ((9/5) * x) + 32
	return f

def fahtocel(x):
	c = ((5/9) * (x - 32))
	return c

if scale == 'c' :
	print('섭씨 %0.1f도는 화씨 %0.1f도이다' % (num, celtofah(num)))
elif scale == 'f':
	print('화씨 %0.1f도는 섭씨 %0.1f도이다.' % (num, fahtocel(num)))

#파일입출력
#실습 1
def Memopad ():
	f = open('input.txt','w')
	while True:
		data = str(input('내용을 한 줄씩 입력하세요'))
		if data != 'end':
			f.write((data+'\n'))
		else:
			f.close()
			print('파일을 저장하였습니다.')
			break
	f = open('input.txt','r')
	mlines = f.readlines()
	for line in mlines:
		print(line)
	print('이 파일을 %d행으로 구성되어있습니다' % len(mlines))
#실습 2
import os
os.chdir('C:/Users/lunar/Downloads')
f = open('score.csv','r',encoding='utf-8')
while True:
	line = f.readline()
	if line =='':break
	v = line.split(',')
	v = v[:-1]
	try:
		int(v[0])
		for i in range(4) :
			v[i] = int(v[i])
		dict = {}
		dict[v[0]] = [v[1:4],v[1]+v[2]+v[3],(v[1]+v[2]+v[3])/3]
		print("%s학생의 총점은 %d점, 평균은 %0.2f점입니다."
		%(v[0],dict[v[0]][1],dict[v[0]][2]))
	except ValueError:
		continue

# 과제 1
f1 = open('test.txt','w')
data = str(input("데이터를 입력하세요"))
f1.write(data)
f1.close()
f2 = open('test.txt','r')
print(f2.read())

# 과제 2
def lotto_generator(x):
	import random
	valist = list(range(1,46))
	lottery_nums = []
	for i in range(6):
		random.shuffle(valist)
		val  = random.choice(valist)
		lottery_nums.append(val)
	print("%s회 :" % x , end = " ")
	for i in lottery_nums:
		print(i,end = " ")
	return lottery_nums

def lotto_stat(x):
	results = {}
	for i in range(1,46):
		results[i] = 0
	lotto_generator(x)
	for i in lottery_nums:
		results[i] += 1
	return results

for i in range(1,4):
	results = lotto_stat(i)
for i in results.keys():
		print("%s : %d회" % (i,results[i]))
print(sorted(results, key= lambda c :results[c], reverse=True)[:6])


# 과제 2_1
def lotto_generator(x):
	import random
	valist = list(range(1,46))
	lottery_nums = []
	for i in range(6):
		random.shuffle(valist)
		val  = random.choice(valist)
		lottery_nums.append(val)
	print("\n%s회 :" % x , end = " ")
	for i in lottery_nums:
		print(i,end = " ")
	return lottery_nums

def lotto_stat(x):
    results = {}
    for i in range(1,46):
        results[i] = 0
    for i in range(1,x+1):
        lottery_nums = lotto_generator(i)
    for i in lottery_nums:
        results[i] += 1
    return results   ## 왜 여기서 반복되는걸
    for i in results.keys():
        print("%s : %d회" % (i,results[i]))
        print(4)


this_nums = sorted(lotto_stat(10), key= lambda c :lotto_stat(10)[c], reverse=True)[:6]
print("이 주의 로또 번호 :",end = " ")
for i in this_nums:
    print(i, end = " ")
