## for문(2:05:10): 반복문
# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 {}".format(waiting_no))

#randrange()
# for waiting_no in range(5): #0,1,2,3,4까지 
#     print("대기번호: {0}".format(waiting_no))

# for waiting_no in range(1, 6): #1,2,3,4, 5까지 
#     print("대기번호: {0}".format(waiting_no))


# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks: #데이터타입이 list인 starbucks를 시퀀스에 넣음으로써 starbucks에 있는 모든 요소들이 한번씩 출력됨
#     print("{0}, 커피가 준비되었습니다.".format(customer)) 

# starbucks =["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{}, 커피가 준비 되었습니다.".format(customer))



## while (2:09:34)
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True: #무한루프
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#     index +=1

# customer = "토르"
# person = "Unknown"
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


## continue & break (2:15:00)
# absent = [2, 5] #결석
# no_book = [7] #책을 놔두고옴
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))
    


##한줄 for문 (2:19:11)
#출석번호 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students = [ i+100 for i in students]
# print(students)


#학생 이름을 길이로 변환
# students = ["Iron Man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

#학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


##quiz5
#Coco서비스를 이용하는 택시 기사. 
#50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램 작성

#조건1: 승객별 운행 소요 시간은 5-50분 상의 난수
#조건2: 소요시간 5-15분 사이의 승객만 매칭해야됨

#출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ....
# [ ] 50번째 손님 (소요시간 : 16분)

#내가 한것)
# from random import randint
# customers = [i for i in range(1, 51)]

# for i in customers:
#     time = randint(5, 50)
#     if time >= 5 and time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

#강의에서 한것
# from random import *
# cnt = 0 #총 탑승 승객 수
# for i in range(1,51): # 1~50 이라는 수
#     time = randrange(5, 51) #5 ~50분 사이 소요시간
#     if 5 <= time <= 15: #5-15분 이내 손님, 탑승 수 증가 처리(매칭성공)
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: #매칭 실패
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0}분".format(cnt))



# #함수(2'28"36"')
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
    
# open_account() #함수 호출

# #전달값과 반환값
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {}원입니다.".format(balance))
#         return balance
    
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money- commission #tuple
    

# balance = 0 
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 1000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))



#기본값(2'37"50"')
# def profile(name, age, main_lang):
#     print("이름은: {0} \t나이:{1}\t주 사용 언어: {2}".format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은반 같은 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름은: {0} \t나이:{1}\t주 사용 언어: {2}".format(name, age, main_lang))

# profile("유재석") #age, main_lang를 알려주지 않았지만 기본값으로 출력됨.
# profile("김태호")



# #키워드값(2'41"33"')
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", main_lang = "파이썬", age = 20) #순서가 달라져도 함수의 인자순서대로 출력됨


#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {}\t나이: {}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang4, lang5)
#위의 불편함을 아래 함수와 같이 표현함

# def profile(name, age, *language):
#     print("이름: {}\t나이: {}\t".format(name, age), end = " ")
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "python", "java", "C", "C++", "C#", "Javascript")
# profile("김태호", 25, "kotlin", "swift")


#지역변수와 전역변수
# gun = 10 #전역변수

# def checkpoint(soldiers): #경계근무
#     global gun #전역 공간에 있는 gun사용
#     gun = gun - soldiers
#     print("[함수 내]남은 총: {}".format(gun))
    
# def checkpoint_return(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내]남은 총: {}".format(gun))
#     return gun
    
# print("전체 총: {}".format(gun))
# checkpoint(2) #2명이 경계 근무나감
# print("남은 총:{}".format(gun))



# 표준 입출력(2'59"3"')
# print("python", "java", sep=",", end="?") #print()함수가 끝나면 기본적으로 줄바꿈인데 그걸 end의 값으로 바꿔주는것
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# scores = {"수학":0, "영어":50,"코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust: 왼쪽정렬, rjust:오른쪽정렬, sep: 출력하는것 사이


#은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호:" + str(num).zfill(3)) # zfill:3개공간확보후 빈공간은 0으로 채움 
    
# answer = input("아무 값이나 입력하세요: ") #입력값이 answer에 저장
# print("입력하신 값은 "+answer + "입니다.")



# # 다양한 출력 포맷(3'10"13"')

# # 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) #>오른쪽정렬 <왼쪽정렬
# # 양수 일땐 +로 표시, 음수일땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000000000))
# # 3자리 마다 콤마를 찍어주기, +-부호도 붙이기
# print("{0:+,}".format(1000000000000000))
# print("{0:+,}".format(-1000000000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보
# # 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))



# 파일 입출력(3'17"46"')
# 파일을 열어서 점수정보를 쓰는것
# score_file = open("score.text", "w", encoding="utf8") #open()함수를 실행함으로써 'score.text'파일 저장되고 print문의 내용이 저장됨
# print("수학: 0", file = score_file)
# print("영어: 50", file = score_file) 
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a: append 덮어쓰기
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100") # write()에는 따로 줄바꿈이 없기때문에 \n써줌
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#반복문이 몇줄인지 모를때 
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


# pickle(3'26"27"') 프로그램의 데이터를 파일형태로
# import pickle

# profile_file = open("profile.pickle", "wb") 
# profile= {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") 
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러와서 변수로 사용할수 있게함
# print(profile)
# profile_file.close()


# with (3'30"23"')
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())



# 퀴즈 7 ( 3'33"37"')
# 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# X주차 주간보고 - 
# 부서 : 
# 이름 : 
# 업무 요약:

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오. 
# @조건: 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다. 


# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(" - {0}주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :") 
#         report_file.write("\n업무 요약:")



# 클래스(3'38"9"')

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
# marine1 = Unit("마린",40, 5) # self인자를 제외한 나머지 인자들을 써줌
# marine2 = Unit("마린",40, 5) 
# tank = Unit("탱크", 150, 35)



# __init__ (3'47"5"')
# class Unit:
#     def __init__(self, name, hp, damage): #생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 멤버변수(3'48"35"')
# class Unit:
#     def __init__(self, name, hp, damage): 
#         self.name = name #멤버변수
#         self.hp = hp #멤버변수
#         self.damage = damage #멤버변수
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# #레이스: 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 50)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) #멤버변수를 외부에서 사용

# #마인드 컨트롤: 상대방 유닛을 내것으로 만드는것
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True #객체에 추가로 변수를 생성함. wraith2변수에만 새로운 변수생성되는것이지 생성자에 추가되는것 아님!!

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
    

# # 메소드(3'53"5"')
# class Unit:
#     def __init__(self, name, hp, damage): #생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # 공격 유닛
# # class 내의 함수(메소드)에는 항상 self를 포함해야됨. 
# # self.를 통해 자기 자신의 변수에 접근가능

# class AttackUnit:
#     def __init__(self, name, hp, damage): #생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage)) # self.가 붙지 않은 경우 받아오는 인자의 값을 그대로 사용
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #파이어뱃: 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)



# # 상속(3'59"30"')

# #일반 유닛
# class Unit:
#     def __init__(self, name, hp): #생성자
#         self.name = name
#         self.hp = hp

# # 공격 유닛
# # 일반 유닛과 동일한 멤버변수가 있어서 상속받아사용.
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp) #상속 받아오는 부분
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage)) # self.가 붙지 않은 경우 받아오는 인자의 값을 그대로 사용
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #메딕: 의무병

# #파이어뱃: 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)




# 다중 상속(4'2"54"')
# 여러곳(부모클래스)에서 상속받음

# #일반 유닛
# class Unit: #부모 클래스
#     def __init__(self, name, hp): #생성자
#         self.name = name
#         self.hp = hp

# # 공격 유닛
# class AttackUnit(Unit): #자식클래스
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp) #상속 받아오는 부분
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage)) # self.가 붙지 않은 경우 받아오는 인자의 값을 그대로 사용
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #드랍쉽: 공중 유닛,  수송기. 마린/파이어뱃/탱크 등을 수송. 공격기능 x

# #날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed)) # self.가 붙지 않은 경우 받아오는 인자의 값을 그대로 사용

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
    
# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사. 
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")



























































