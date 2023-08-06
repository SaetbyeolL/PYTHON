# 메소드 오버라이딩(4'10"10"')
# 자식클래스에서 정의한 메소드를 사용하고 싶을때 메소드를 새롭게 정의해서 사용할수 있는데 이걸 오버라이딩


# #일반 유닛
# class Unit: #부모 클래스
#     def __init__(self, name, hp, speed): # speed추가됨
#         self.name = name
#         self.hp = hp
#         self.speed = speed
        
#     def move(self, location): #메소드 추가
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
#             .format(self.name, location, self.speed))

# # 공격 유닛
# class AttackUnit(Unit): #자식클래스
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed) #상속 받아오는 부분
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
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상speed는 0으로 받음
#         Flyable.__init__(self, flying_speed)
        
#     def move(self, location):          #Unit과 동일하게 move()함수 있음
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)    
    
    
# # 벌쳐: 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력 좋음, 공격력 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)


# # 매번 유닛이 지상인지 공중유닛인지 확인하는것 귀찮-> 똑같이 move함수써서 각각의 경우에 알맞게 사용하는것. 
# 입력되는 인자를 보면 어떤 함수에 오버라이딩되는건지 알수 있음. 
# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


# pass(4'17"6"')
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass  #아무것도 안하고 넘어감

# # 서플라이 디폿: 건물. 1개 건물 = 8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
    
# def game_over():
#     pass

# game_start()
# game_over()


# super(4'19"31"')
# class Unit: #부모 클래스
#     def __init__(self, name, hp, speed): # speed추가됨
#         self.name = name
#         self.hp = hp
#         self.speed = speed
        
#     def move(self, location): #메소드 추가
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
#             .format(self.name, location, self.speed))

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)  # 상속 1번째 방법
#         super().__init__(name, hp, 0)     # 상속 2번째 방법: self를 뺴고 쓴다
#                                           # 다중상속일때는 첫번째 상속받는 메소드만 받기때문에 super쓰지말자
#         self.location = location



# 퀴즈
# 주어진 코드를 활용하여 부동산 프로그램을 작성

#(출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

#[코드] 내가 한것
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
        
#     # 매물 정보 표시
#     def show_detail(self):
#         print("총 3대의 매물이 있습니다.")
#         print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

# #생성자코드(내가 만든것)
# saling1 = House("강남", "아파트", "매매", "10억", "2010년")
# saling2 = House("마포", "오피스텔", "전세", "5억", "2007년")  
# saling3 = House("송파", "빌라", "월세", "500/50", "2000년")    

# #실행코드(내가 만든것)
# saling1.show_detail()
# saling2.show_detail()
# saling3.show_detail()



# 강사가 한것
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
        
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
        

# # 초기화
# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")  
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")  
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# # 출력 코드
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()















































