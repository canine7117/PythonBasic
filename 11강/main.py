# 수업 시자구

class Dog :
    name = "코코"
    age = 2
    def bark(self):
        print('멍멍') 
    def move(self):
        print('움직인다')
    def eat(self):
        print('움얌얌')

dog1 = Dog() 
dog1.name = '코코'
dog1.age = 2

dog2 = Dog() 
dog2.name = '두리'
dog2.age = 4
dog2.weight = 10
 
dog1.bark()
dog1.move()
dog1.eat()

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

class Dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def bark (self):
        print(' 멍멍')
    def move(self):
        print('움직이다')

dog1 = Dog ('코코', 2)
dog2 = Dog ('두리', 4)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age) 


class Dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def bark (self):
        print('{}가 월월워루얼우렁울러우러ㅓ우러우러우월워루얼  ' .format(self.name))
    def move(self):
        print('움직이다')

dog1 = Dog('코코',2)
dog2 = Dog('두리',4)
dog3 = Dog('하리',1)
 
dog1.bark() 
dog2.bark() 
dog3.bark()

# 커피를 너무 많이 마셨나봐요
# 심장이 막 두근대고 잠은 잘 오지 않아요
# 한참 뒤에 별빛이 내리면
# 난 다시 잠에 들 순 없겠죠
# 지나간 새벽을 다 새면
# 다시 네 곂에 잠들겠죠
# 그대 품에 잠든 난 마치 천사가 된 것만 같아요
# 난 그대 품에 별빛을 쏟아 내리고
# 은하수를 만들어 어디든 날아가게 할거야
# cause I'm a pilot everywhere
# cause I'm a pilot everywhere
# shooting star oh lighting star
# 즐게 my galaxy
#2절
# 어제는 내가 기분이 참 좋아서
# 지나간 행성에다가 그대 이름 새겨 놓았죠
# 한참 뒤에 별빛이 내리면 그 별이 가장 밝게 빛나요
# 지나간 새벽을 다 새면

#이건 세상에서 제일 비싼 단독공연
# 관객은 너 하나
# 이제 곧 화려한 막이 내리기 전에
# 그저 몇가지만 주의해줘요
# 세상에서 제일 편한 옷을 갈아입고
# 제일 편한 자리에 누워
# 





class Dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def bark (self):
        print('{}가 월월워루얼우렁울러우러ㅓ우러우러우월워루얼  ' .format(self.name))
    def move(self):
        print('움직이다')
    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age)
        return sentence        
dog1 = Dog('코코',2)
dog2 = Dog('두리',4)
print(dog1)
print(dog2)

#짜중낭

result = 0
def 더하기(num):
    global result
    result += num
    return result

print(더하기(3))
print(더하기(4))

class Calculator:
    def __init__(self):
       self.result = 0
    def 더하기 (self, num):
        self.result += num
        return self.result

call = Calculator =  0

print(call.더하기(3))
print(call.더하기(4))

class Calculator:
    def __init__(self):
        self.result = 0
    def 더하기 (self, num):
        self.result += num
 





