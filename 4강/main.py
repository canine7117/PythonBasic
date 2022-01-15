money = 10000
if money == 10000:
   print("택시를 타고 가라")
else:
     print("걸어가라")


name = input('당신의 이름은?')
age = int(input('당신의 나이는?'))

print ('당신은'+ name + '이고' , age, '살입니다.')
print ('당신은', name , '이고' , age, '살입니다.')
print ('당신은 {} 이고 {} 살입니다.'.format(name,age))

print('가위 바위 보 중 하나를 내주세요>')
mine = input()
print( 'mine:', mine)

mine = input ('가위 바위 보 중 하나를 내주세요>')
print('minhe:', mine)

date = input('오늘 날짜:')
print('오늘의 날짜는', date, '입니다.')

date = input ('오늘 날짜:')
year = date[0:4]
month = date [5:7]
day = date [8:10]
print('년"', year)
print('월"', month)
print('일"', day)

x = 3
y = 2
print(x > y)
print(x < y)
print(x ==y)
print(x != y)
print(x >= y)
print(x <= y)

if 3<5:
    print("조건식이 True")
if 3>5:
    print("조건식이 False")

apple = 3
if apple >= 5 :
    print("사과를 나누어 먹는다")
else:
    print("사과를 혼자 먹는다")
    
money = 10000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

rank = input('몇 등인가요(1또는2)?')

if rank == '1': 
    print('TV를 보며 편안히 휴식')
    
if rank == '2': 
     print('설거지 당첨!')



grade = int(input("몇학년인가요(1~6)?"))
if grade >= 2 and grade <= 4:
    print("햄버거를 주세요")
else:
    print("김밥을 주세요")

money = int(input("가지고 있는 돈 :"))
distance = int(input(" 목적지와의 거리 :"))
weather = input("날씨:")
if money >= 10000 and distance >= 100 and weather == '비':
    print("택시를 타고 가라")
else: 
    print("걸어가라")
