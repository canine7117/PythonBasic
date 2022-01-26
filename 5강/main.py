data = input("입력값:")
if int(data)-20 > 255:
    print(255)
elif int(data)-20 < 0:
    print(0)
elif 0< int(data)-20 <255:
    print(int(data)-20)
    
print (3>5)
print (3<5)
print (3==5)
print (3!=5)

x=4
print(1<x<5)

print((3==3)and (4!=3))

data = input("입력값:")
if int(data) % 2 == 0:
    print("짝수")
else:
    print("홀수")


data = input("입력값:")
if int(data)+20 < 255:
    print(int(data)+20)
else:
    print("255")
