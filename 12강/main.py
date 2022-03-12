class Animal:
    def eat(self):
       print('먹는다')
    def move(self):
        print('움직인다')
    def 응양(self):
        print('인간 = 동물')

class Dog(Animal):
    def bark(self):
        print('멍멍')

    def shake(self):
        print('꼬rㅣ를 흔들ㄷr')
    def cute(self):
        print('아임 쏘 큩이 시크뤳 초코뤳 듀듀..?????★☆★') 

    
dog = Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()
dog.cute()

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')

class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name,age)
        self.owner = owner
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence = '이름:{},나이:{},주인:{}'.format(self.name,self.age,self.owner)
        return sentence


animal = Animal('동물',1)
animal.eat()
dog = Dog ('코코', 2, '홍길동')
print(dog.name, dog.age, dog.owner)
print(dog)

# 아니 웃긴ㄱ게 가사중에 쥦쥦쥣짓쥦ㅈ짓쥐ㅅ  지니엿ㅅㅡ 이거 번역하면 ㅊ . 처 . ㅊ처.천.첝.천재 인ㄷ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅊ.천.ㅊ천재놈아 이거라ㄱ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

dog = Dog ('코투',  86678768686867867867867, '홍길동')
print(dog.name, dog.age, dog.owner)
print(dog)

class Animal:
    def __init__(self, age):
        self.age = age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')

class Bird(Animal):
    def __init__(self, age):
        super().__init__(age)

    def eat(self): 
        print('새가 밥을 먹는다')
    def move(self):
        print('새가 몸을 움직인다')
    def __str__(self):
        sentence = '나이:{}'.format(self.age)
        return sentence

class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(age)
        self.name = name
        self.owner = owner
    def eat (self):
        print('강아지가 밥을 먹는다')
    def move(self):
        print('강아지가 몸을 움직인다')
    def __str__(self):
        sentence = '이름:{},나이:{},주인:{}'.format(self.name,self.age,self.owner)
        return sentence

animal = Animal(1)
animal.eat()
dog = Dog ('코코', 2, '홍길동')
print(dog.name, dog.age, dog.owner)
print(dog)
bird = Bird (12222)
print(bird)


class Human:
    def eat(self):
        print('먹는다')
    def poop(self):
        print('배설물')
    
class Teacher(Human):
    def 연장(self):
        print('수업시간을 연장한다!')
    def 쉬는시간(self):
        print('쉬는시干')

class Student(Human):
    def zzanda(self):
        print('水업 시間에 zzㅐnnnda!')
    def 아이디어고갈(self):
        print('許有鬒이/가 아이디어 고갈을/를 맞았다! 효과는 미미햇다. 호호 ')

teacher = Teacher()
teacher.쉬는시간()
teacher.연장()
teacher.poop()

student = Student()
student. zzanda()
student. 아이디어고갈()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
student. zzanda()
























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































