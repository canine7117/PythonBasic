import random

num1 = random.randint(0,100)
num2 = random.randint(0,100)

print('숫자 1 : {0}, 숫자 2 : {1}'.format(num1,num2))
com = num1 + num2
count =0
while True:
    count += 1
    print('두 수의 더하기 값은? ({} 번째 도전)'.format(count))
    user =int(input('당신의 답은?'))

    if user>com:
        print('정답보다 크다')
    elif user<com:
        print('정답보다 작다')
    else:
        print('정답입니다')
        break
       
  
a = 0
while a < 10:
    a = a +1
    if a % 2 == 0:
        continue
    print(a)


a = 0
while a < 10:
    a = a+1
    if a == 5:
        print ('{}입니다.'.format(a))
        break
    print(a)

import random

com = random.randint(0, 100)
count = 0

#print(com)
print('0~ 100까지의 숫자를 입력해주세요')
print('-1을 누르면 포기할 수 있으며 함께 정답을 알려줍니다.')
print('10번의 기회동안 정답을 찾지 못한다면 게임은 실패로 돌아갑니다.')

while True :
    count = count + 1   
    print("{0}번째 도전". format(count))
    if count > 10:
        print('실패하셨습니다. 도전할 수 잇는 기회를 모두 사용하셨습니다. ')
        print(com)
        break
       
    user = int(input('당신의 선택은?'))     
    if user == -1:
        print('포기하셨군요 . 정답은 아래 있습니다 :D')
        print(com)
        break 

    #print(user)
    if user > com:
        print('정답보다 크다')
    elif user < com:
        print('정답보다 작다')
    else:
        print('정답입니다!')
        break

