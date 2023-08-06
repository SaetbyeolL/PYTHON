## 자료형
# print("풍선")
# print("풍선"*9)

##random함수
# from random import *
# print(int(random()*10))
# print((random()*10))
# print(int(random()*45)+1)

#quiz
# from random import *
# print(int(random()*28)+4)
# print("오프라인 스터디 모임 날자는 매월 ",(int(random()*28)+4),"일로 선정되었습니다.")
# date=randint(4,28)
# print("오프라인 스터디 모임 날자는 매월 "+str(date)+"일로 선정되었습니다.")


##문자열
# sentence ='나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요
# """
# print(sentence3)


##슬라이싱: 필요한 정보만 활용하는것
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("년 : "+jumin[0:2]) #0부터 2직전까지
# print("월 : "+jumin[2:4])
# print("일 : "+ jumin[4:6])
# print("생년월일 : "+ jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 : "+ jumin[7:]) #7번째부터 마지막까지
# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지


##문자열 처리 함수
# python ="Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index) #첫번째 n의 위치
# index = python.index("n", index+1) #index+1: 검색을 시작할 위치
# print(index) #두번째 n의 위치

# print(python.find("Java")) # 값이 없을경우 -1을 반환
# #print(python.index("Java")) # 값이 없을 경우 오류가 나서 그 이후에 나오는 print도 출력X
# print("hi")

# print(python.count("n")) # 문자열에서 원하는 값이 몇개 나오는지


##문자열 포맷(1:00:57)
# print("a"+"b")
# print("a", "b")
#방법1
# print("나는 %d살입니다" % 20)
# print("나는 %s을 좋아해요. " % "파이썬") #문자열: 정수, 문자로 가능
# print("Apple은 %c로 시작해요." % "A") #문자(한글자)
# print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

#방법2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) 

#방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간")) #변수처럼 사용가능

#방법4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
"""
f-string을 사용하여 문자열을 출력합니다. 
중괄호 {} 안에 표현식을 작성하면 해당 표현식이 평가되어 문자열에 삽입됩니다.
f-string을 사용하면 변수의 값을 손쉽게 문자열에 삽입할 수 있습니다. 
중괄호 {} 안에 표현식을 작성하면 해당 표현식이 자동으로 평가되어 문자열에 포함됩니다. 
이를 통해 보다 간결하고 가독성 좋은 코드를 작성할 수 있습니다.
"""


##탈출 문자
#\n: 줄바꿈
# print("백문이 불여일견 \n 불견이 불여일타")

#\" \' : 문장 내에서 따옴표
# print("저는 '나도코딩' 입니다")
# print('저는 "나도코딩" 입니다')
# print("저는 \"나도코딩\" 입니다")

#\\ : 문장 내에서 \으로 바뀜
# print("C:\\Users\\saetb\\OneDrive\\바탕 화면\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
#print("Red Apple\rPine") #커서를 맨앞으로 이동해서 그 문자길이만큼 출력됨

#\b : 백스페이스(한글자 삭제)
#print("Redd\bApple")

#\t : tab
# print("Red\tApple")



##Quiz)사이트별로 비밀번호를 만들어주는 프로그램 작성
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                  (nav)             (5)            (1)           (!)
# 예) 생성된 비밀번호 : nav51!

# url = "http://naver.com"
# my_str = url.replace("http://", "") #규칙1
# print(my_str)
# my_str = my_str[:my_str.index(".")] #규칙2: my_str에서 .이 나오기 전까지 출력
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다.".format(url, password))



## 리스트 : 순서를 가지는 객체의 집합[]

#지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway=["유재석", "조세호", "박명수"]
# print(subway)

# #조세호가 몇 번째 칸에 타고 있는지
# print(subway.index("조세호"))

# # 하하가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") #append 마지막에 추가
# print(subway)

# #정형돈을 유재석과 조세호 사이에 넣음
# subway.insert(1, "정형돈")
# print(subway)

# #지하철에 잇는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #하하만 출력됨
# print(subway)

# print(subway.pop()) 
# print(subway)

# print(subway.pop()) 
# print(subway)

# print(subway.pop()) 
# print(subway)

# #같은 이름의 사람이 몇명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)


#다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
#print(mix_list)

#리스트 확장
# num_list.extend(mix_list) # 두 list를 연결
# print(num_list)



##사전 : 키에 대한 중복이 허용되지 않음
# cabinet = {3:"유재석", 100:"김태호"} # key = 3, value = "유재석"
# print(cabinet[3])
# print(cabinet[100])

#print(cabinet.get(5)) #없는 key를 넣으면 error남
# print(cabinet.get(5,"사용 가능")) #key값이 없으면 "사용 가능"이 대체함

# print(3 in cabinet) #3이라는 값이 cabinet에 있으면 True 없으면 False

# cabinet ={"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국" #값을 업데이트
# cabinet["C-20"] = "조세호" #값을 업데이트
# print(cabinet)

#떠난 손님
# del cabinet["A-3"]
# print(cabinet)

#key들만 출력
# print(cabinet.keys()) #dict_keys(['B-100', 'C-20'])

#value들만 출력
# print(cabinet.values()) #dict_values(['김태호', '조세호'])

#key, value 쌍으로 출력
# print(cabinet.items()) #dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
# cabinet.clear() #다지움
# print(cabinet)



##튜플 : 내용 변경이나 추가 x. 그러나속도가 list보다 빠름. 변경되지 않는 목록 사용할때. 
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# menu.add("생선까스") #값추가 안됨

# name = "김종국"
# age = 20
# hobby ="코딩"
# print(name, age, hobby)

# name, age, hobby = "김종국", 30, "코딩" #한번에 값선언 가능
# (name, age, hobby) = ("김종국", 30, "코딩") #튜플
# print(name, age, hobby)



## 집합(set): 중복이 안되고, 순서가 없음(중요하지않음)
#my_set = {1,2,3,3,3}
#print(my_set) #중복이 허용되지 않기 때문에 1,2,3만 출력됨

# set: 파이썬 내장 데이터타입. 중복허용하지 않고 순서가 없는 요소들의 모음
#java={"유재석", "김태호", "양세형"}
#python = set(["유재석", "박명수"]) #list를 집합으로 변환하고 이를 변수 'python'에 할당

#교집합 (java와 python 모두 할 수 있는 개발자) : AND
#print(java & python)
#print(java.intersection(python))

#합집합(java할 수 있거나 python 할 수 있는 개발자) : OR
#print(java | python)
#print(java.union(python))

#차집합(JAVA할 수 있지만 PYHTON은 할 줄 모르는 개발자)
#print(java - python)
#print(java.difference(python))

#python 할 줄 아는 사람 늘어남
#python.add("김태호")
#print(python)

#java를 까먹었다
#java.remove("김태호")
#print(java)



##자료 구조의 변경
#커피숍: 중괄호 {}를 사용하여 set을 생성
# menu = {"커피", "우유", "주스"} #{"커피", "우유", "주스"}라는 요소를 가진 set 객체를 변수 menu에 할당

# print(menu, type(menu)) #{'주스', '우유', '커피'} <class 'set'>

# menu =list(menu)
# print(menu, type(menu)) #['주스', '우유', '커피'] <class 'list'>

# menu=tuple(menu)
# print(menu, type(menu)) #('주스', '우유', '커피') <class 'tuple'>


#파이썬에서 배열과 같은 기능수행하는 데이터타입: list
#list: 내장 데이터 타입 중 하나로, 순서가 있는 요소들의 모음 
# 리스트는 대괄호 []를 사용하여 생성하며, 각 요소는 쉼표로 구분 
# 리스트는 변경 가능한(mutable) 시퀀스 타입이므로 요소를 추가, 삭제, 수정 가능



#Quiz) 댓글이벤트. 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰. 추첨 프로그램 작성.
#조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
#조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#조건3: random 모듈의 shuffle과 sample을 활용

#(출력 예제)
#-- 당첨자 발표 --
#치킨 당첨자 : 1
#커피 당첨자 : [2,3,4]
#-- 축하합니다 --

#(활용 예제)
# from random import *
# lst =[1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


# from random import *
# ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #list
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 :", sample(ID, 1))
# print("커피 당첨자 :", sample(ID, 3))
# print("-- 축하합니다 --")

# from random import *
# users = range(1,21) #range라는 데이터타입
# print(type(users))
# users=list(users)
# print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")


## if
# if 조건:
#     실행명령문

# weather = input("오늘 날씨는 어때요? ") #입력
# if weather =="비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10 :
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")






























