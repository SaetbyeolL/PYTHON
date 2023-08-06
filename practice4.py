# pip install(5'40"32"')
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())



# 내장함수(5'46"5"')

# input: 사용자 입력 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))


# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))



# 외장함수(5'5"45"')
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) #폴더 생성
    print(folder, "폴더를 생성하였습니다.")


























