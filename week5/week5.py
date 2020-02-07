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
            results[i] = results[i] + 1
    print("\n")
    for i in results.keys():
        print("%s : %d회" % (i,results[i]))
    return results


results = lotto_stat(100)

this_nums = sorted(results, key= lambda c :results[c], reverse=True)[:6]

print("이 주의 로또 번호 :",end = " ")
for i in this_nums:
    print(i, end = " ")
