from cmd import PROMPT
from re import T
#number = 0
#max = int (input())
#while number < max:
 #   number = number + 1
 #   print(number)

print ("숫자 두 개를 작은수부터 입력해주세요.")
min = int(input())
max = int(input())
for number in range (min, max+1,1):
    print(number)

max = int(input())
for number in range (1, max+1 , 3):
    print(number)

for number in range (1,10):
    string = '{}*{}={}'. format(2, number, 2*number)
    print(string)

for 단 in range(2,10):
    print('{}단 시작'.format(단))
    for number in range (1,10):
        string = '{}*{}={}'. format(단, number, 단*number)
        print(string)
    print('{}단 종료', format())
                   
시작단 = int(input('구구단 시작 단을 입력하세요(1~9):'))
끝단 =int(input('구구단 끝 단을 입력하세요(1~9):'))

for 단 in range(시작단, 끝단+1):
    for number in range(1,10):
        string = '{}*{}={}'.format(단,number,단*number)
        print(string)

#number= 0
#while number < 10:
    #number = number + 1
   # print ( number)

for number in range (1,13,1):
    print("{}월".format(number))
number = 1
while number <= 10:
    print ( number)
    number = number + 1


prompt = """
100을 입력하면 종료가 되는 프로그램입니다.
과연 당신은 언제 100을 입력할까요?
Enter number: """

#number = 0


#while number != 100:
 #   print(prompt)
  #  number = int(input())

print("숫자를 두개를 작은수부터 입력해주세요.")
min = int( input())
max = int(input())
while min <= max :
    print(min)
    min =min+1

#while True:
 #   print ("Ctrl+C를 눌러야 While문을 빠져나갈 수 있습니다. 이 문장은 계속 반복됩니다...")


score = int(input("점수:"))
if 0 <= score < 20 :
    print("E등급")
elif 21 < score < 40 :
    print("D등급")
elif 41 < score < 60 :
    print("C등급")
elif 61 < score < 80 :
    print("B등급")
elif 81 < score <= 100 :
    print("A등급")

hit = 0
while hit < 100000:
    hit = hit+1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 100000:
        print("나무가 넘어갔습니다!")
    elif hit == 99999:
       print("나무가 곧 넘어갈 것 같습니다!")
    elif hit % 100 == 0 :
        print("나뭇잎이 떨어졌습니다!")
