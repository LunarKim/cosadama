''' 다들 2,3,4,5번은 잘 푸셨습니다. 
그래서 힘들어하신 1번 문제에 대한 답안만 적었습니다. 
다른 문제들은 다른 분들의 코드를 잘 참고해주시면 되고, 
1번 문제는 다들 count를 셀 때 오류가 있었던 것 같은데 
잘 코드 리뷰를 해보시길...! '''


# 1. 랜덤 숫자 맞추기

import random
number = random.randint(1, 20)
count = 0

while True:
    user = int(input('내가 생각한 숫자를 맞추세요. '))
    if user > number:
        print('숫자가 작아요. 큰 숫자를 다시 넣으세요.')
    elif user < number:
        print('숫자가 커요. 작은 숫자를 다시 넣으세요.')
    else:
        print('정답!')
        break
    count += 1

count += 1
print(count, '회 만에 맞았습니다.', number, '이에요.')
