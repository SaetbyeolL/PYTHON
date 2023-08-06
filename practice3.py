# 예외처리(4'50"12"')

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err: # ValueError와 ZeroDivisionError를 제외한 모든 에러
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)



# 에러 발생시키기(4'58"14"')
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))    
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")



# 사용자 정의 예외처리(5'1"6"')

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))    
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)



# finally(5'4"27"'): try구문에서 무조껀 실행되는 부분

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))    
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")
    


# 퀴즈9(5'7'00"')
# 시스템 코드를 확인하고 적절한 예외처리 구문넣기

# 조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
#     출력 메시지: "잘못된 값을 입력하였습니다."
# 조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#     치킨 소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#     출력 메시지: "재고가 소진되어 더 이상 주문을 받지 않습니다."

# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# chicken = 10
# waiting = 1
# loop = 1
# while(loop):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇마리를 주문하시겠습니까?"))
        
#         if order > chicken: #남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldOutError("남은 치킨양은 {0}마리 입니다".format(chicken))
    
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as err:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         print(err) #남은 치킨양은 0마리 입니다 <- 이게 출력됨. 
#         loop = 0
        


#-------------------------------
#강사가 한 답변

# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇마리를 주문하시겠습니까?"))
            
#         if order > chicken: #남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
        
#         elif order <= 0:
#             raise ValueError    
        
#         else:
#             print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
        
#         if chicken == 0:
#             raise SoldOutError
    
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break



# 모듈(5'14"22"')
# import theater_module   #.py는 뺴줌
# theater_module.price(3) #3명이서 영화 보러 갔을때 가격
# theater_module.price_morning(4) #4명이서 조조할인 영화 보러갔을때 가격

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# from theater_module import * # theater_module의 모든것을 사용하겠다
# from random import *
# price(3)
# price_morning(4)
# price_soldier(5)


# from theater_module import price, price_morning #모듈의 어떤 함수만 사용할지 정할수있음
# price(3)
# price_morning(4)



# 패키지(5'24"10"')
# import travel.thailand # 바로 class를 연결할 수 없음
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage  
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()



# __all__ : 모듈이나 패키지의 속성 중에서 외부로 노출하고자 하는 것들을 명시적으로 지정하여 다른 사용자가 모듈을 더 쉽게 사용

# from travel import * #이렇게 명시되어 있지만 다 들고올수있는게 아니고 명시된것만 사용됨. travel-'__init__'폴더에 명시함
# #trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()



# 모듈 직접 실행(5'34"16"')
# from travel import * 
# #trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()



# 패키지, 모듈 위치(5'37"00"')
# from travel import *
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))



















