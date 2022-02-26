
점수들 = [90,25, 67, 45, 80]
number = 0
for 점수 in 점수들:
    number = number + 1
    if 점수 >=60:
        print("{}번 학생은 합격입니다.".format(number))
    else:
        print("{}번 학생은 불합격입니다.".format(number))
        
과일들 = ["사과", "귤","복숭아","포도"]
for 과일 in 과일들:
    print(과일)

완뚜스리= [  10,20,30]
for 완뚜스리 in 완뚜스리:
    # print("{}\n------".format(완뚜스리))
    print(완뚜스리)
    print('------')

멙뉴들 = [ "김밥","라면","튀김"]
for 멙뉴 in 멙뉴들:
    print("오늘의 메뉴 : {}메뉴.".format(멙뉴))

# 즐거운 플리~
# Lucy - 조깅 / 볼사 - 우주를 줄게 / cups / WTF / juice / Alone / 태연 - I can't control myself , INVU / 최예나 - smiley 
#
#  볼사 - 우주를 줄게 / 가사
# 커피를 너무 많이 마셨나봐요
# 심장이 막 두근대고 잠은 잘 오지 않아요
# 한참 뒤에 별빛이 내리면 난 다시 잠에 들순 없겠죠
# 지나간 새벽을 다새면 다시 네곁에 잠들겠죠
# 그대 품에 잠든 난 마치 천사가 된 것만 같아요
# 난 그대 품에 별빛을 쏟아 내리고
# 은하수를 만들어 어디든 날아가게 할거야
# Cause I'm a pilot oh everywhere
# Cause I'm a pilot oh shooting star
# shooting star , oh shooting star
# 줄게 my galaxy
# 
#  최예나 - smiley
# 울지마 울지마 어린아이 같이
# 웃는 게 웃는 게 이기는 거라구
# 
#  Lucy - 조깅
# 내가 가고 싶은 대로만 간다면
# 그저 틀린 길만 나올까
# 오늘도 우린 쉬지 않고 달렸잖아
# (마라톤 하듯이)
# 그러다 머리 한번 핑 돌아
# 가끔 한번씩 동네 한번 빙 돌아
#
#  I'm not a hero
# 모래먼지 가득한 도심 속에 서 있는 강아지 소년
# I'm not a hero
# 하찮은 내 존재
# 아무것도 지킬 수 없는 loser
# 멀어지는 당신의 모습을
# 다시는 놓치기 싫어 - 
# 아아아 -
#
#  픽셀리 (뜰넴) - pray for you
# 지나간 추억은 뒤로한채
# 지금부터 pray for you -
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 즐거운 뜰팁 ~
#
#  혁명
# 아무것도 지키지 못한 에투알 왕국의 황제 라더의 마지막 명이다.
# 저도 폐하의 명을 한 번 어겨보려 합니다.
#  헤드라이너
# 모두 당신의 선택입니다 -, 헤드라이너.
#  밤보눈
# 당신 .. 인간 아니지 ?
#  이방인
# 제가 어떻게 감히 폐하의 명을 어기겠습니까!
# 파수꾼 라더, 당신은 날 이해할 수 있죠?
#  뜨리미널 - 인형공방
# 모든 걸 원래대로 되돌려놓고 싶었어.
# 너희들이 건방졌을 뿐이야.
#  워터플래그 
# 각별아, 집에 가자.
# * 명언 없는 뜰팁 상극들 ( 단기 ,장기 다)
# 블라인드 - 유토피아 , 황금사과 , 귀신의 집 , 뱀파이어 대저택 , 5명의 후계자 중 진짜를 찾아라 
# 미수반 - 매화꽃 필 무렵 , 불타오르는 월야 서커스 , 
# 혁명 워플 헤드라이너 밤보눈 미수반 마오블 뜨리미널 우리 왜 만났나요 이방인 블라인드 럭키 스카이블럭 
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ



from time import time
from 수학 import 더하기,빼기
print(더하기(3,4))


from 수학 import *
print(더하기(3,4))

import time
print('현재시각:', time.time())

def manyloop(max):
    t1 = time.time()
    for a in range(max):
        pass
    t2 = time.time()
    print(t2-t1,'초 경과')

number = int (input('숫자를 입력하세요:'))
manyloop(number)

import time
current = time.ctime()
print(current)메인

수학

def 더하기(a,b):
    return a+b

def  빼기(a,b):
    return a-b
