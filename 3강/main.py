def 시리얼먹기(우유, 시리얼, 그릇, 숟가락):
    print("{}을 {}에 넣습니다.".format (시리얼, 그릇))
    print("{}을 {}이 담긴 {}에 따릅니다.".format(우유, 시리얼, 그릇))
    print("{}으로 {}과 {}를 떠서 먹습니다.".format(숟가락,시리얼,우유))
    return "{} 1리터, {} 500그램 남았습니다.".format(우유, 시리얼)
   
결과 = 시리얼먹기("우유", "시리얼", "그릇", "숟가락")
print (결과)

#연습문제들~~~~~~~~~~~~~
def hello():
    print("안녕하세요")
hello()

def message():
    print("A")
    print("B")
    
message()
print("C")
message()

def say1(name):
    string = '안녕하세요?' + name + '님'
    return string

def say2(name):
     string = '안녕하세요?' + name + '님'
     print(string)

name = "홍길동"
string = say1(name)
print(string)

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def divi(a, b):
    return a//b

a = 6
b = 3
print(add(b,a))
print(sub(b,a))
print(mul(b,a))
print(divi(b,a))

# ___브라우니만들기 (버터,초콜릿,믹스넛,바닐라,달걀):
#초콜릿을 냄비에 넣고 녹인다
#버터를 잘게 잘라서 냄비에 넣고 녹인다
#그릇에 달걀을 풀어 넣는다
#달걀을 푼 그릇에 녹인 초콜릿과 바닐라를 넣고 잘 섞는다 오븐그릇에 담은 다음 믹스넛을 고르게 뿌린다
#오븐에 180도로 25~30분 굽는다
#return 만든브라우니갯수
#
#나의 브라우니 = 브라우니 만들기(250,2,100,50,3)

def 브라우니만들기 (버터,초콜릿,바닐라, 믹스넛,달걀):
    print ("{}을 냄비에 넣고 녹인다".format(초콜릿))
    print ("{}를 잘게 잘라서 냄비에 넣고 녹인다".format(버터))
    print ("그릇에 {}을 풀어 넣는다".format(달걀))
    print ("{}을 푼 그릇에 녹인 {}과 {}를 넣고 잘 섞는다 오븐그릇에 담은 다음 {}을 고르게 뿌린다".format(달걀, 초콜릿, 바닐라, 믹스넛))
    print ("오븐에 180도로 25~30분 굽는다")
    return "만든브라우니갯수"

브라우니만들기 ("버터","초콜릿","바닐라", "믹스넛","달걀")

#추가문제!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def 안녕():
    print("안녕,함수!")


안녕()

안녕()
안녕()

안녕()
안녕()
안녕()
안녕()
안녕()

def result():
    print("{}+{}={}".format(a,b,result))
    
add(10,5)

#return "{} 1리터, {} 500그램 남았습니다.".format(우유, 시리얼)

def add_10(a):
    return a+10

def print_with_smile(a):
    return ("{}:D ".format(a))

def print_operation(a, b):
    print("{} + {} = {}".format(a, b, a+b))
    print("{} - {} = {}".format(a, b, a-b))
    print("{} * {} = {}".format(a, b, a*b))
    print("{} // {} = {}".format(a, b, a//b))


a = 10
b = 10
print(add_10(a))
print(print_with_smile(a))
print(print_operation(a,b))
                
