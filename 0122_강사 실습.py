# # 문자열 메소드 실습 > print로 출력하기
# a = " Practice makes perfect "

# #1. 문자열 a에서 'e'의 개수 세기 ★★★
# print(f"Q1. {a.count('e')} e 개수 세기")

# #2. 문자열 a에서 i의 위치 찾기(2가지 방법) ★★★★★
# print(f"Q2_1. {a.find('i')} i 위치 찾기 _ find") # 없으면 -1 반환
# print(f"Q2_2. {a.index('i')} i 위치 찾기 _ index") # 없으면 오류 발생

# #3. 문자열 a의 문자 사이에 .(점) 삽입 ★★
# a_dot = '.'.join(a)
# print("Q3", a_dot)

# #4. 문자열 a를 공백 기준으로 분리하기 ★★★★★
# spl = a.split()
# print("Q4",spl,"split으로 분리하기")

# #5. 문자열 a에서 'makes'를 'made'로 바꾸기 > 원본은 변경되지 않는다.
# a_rep=a.replace("makes","made")
# print("Q5",a_rep,"made로 대체하기")

# #6. 문자열 a를 대문자에서 소문자로 바꾸기, 소문자에서 대문자로 바꾸기
# print(a.lower())
# print(a.upper())
# print("Q6", a.swapcase(),"대소문자 서로 변경")

# #7. 문자열 a의 양쪽 공백 삭제하기 ★★★
# a_strip = a.strip()
# print("Q7", a_strip,"양끝 공백 삭제")

# #8. 입력된 시각(14:43:20)에서 시간 부분만 보여주기 ★★★★★
# from datetime import datetime

# now_time= str(datetime.now()).split()[1].split(":")[0]
# print("Q8", now_time,"현재 시각의 시 표시하기")

# #8-1 주민번호(890927-1234567)에서 생일만 보여주기 , 성별 보여주기
# #(1)
# birthday = '890927-1234567'
# birthday_split = birthday.split('-')
# print("생일만 뽑기",birthday_split[0][2:])
# #(2)
# #print(input().split('-')[0][2:])
# #8-1-1 성별 뽑기
# birthday ='890927-1234567'
# birthday_split2 = birthday.split('-')
# if birthday_split2[1][0] == "1":
#     print("남자")
# elif birthday_split2[1][0] =="2":
#     print("여자")
# else:
#     print("젊은이")


# #8-1 강사님 answer
# a = '890927-1234567'.split('-')
# print(a[0][2:],"생일")
# print(a[1][0],"성별")

# text = "            Hello       World ~  "
# print(text.find("W"))
# print(text.strip().find("W"))




# # 반환하지 않는 메서드 ( void methods)
# # 리스트 메서드 실습 > print(a)
# a = ['b', 'a', 'n', 'a', 'n']

# #1. 리스트 a의 마지막에 'a' 추가하기 ★★★★★ > stack(후입선출)
# a.append("a")
# print(a)
# #2-1. 리스트 a를 오름차순으로 정렬 > 원본 변경 ★★★
# a.sort()
# print("Q2-1",a)

# #3. 리스트 a를 내림차순으로 정렬
# a.sort(reverse=True)
# print("Q3",a)
# #4. 리스트 a를 역순으로 뒤집기
# a.reverse()
# print("Q4",a)
# #5. 리스트 a에서 문자 'a' 삭제하기
# a.remove('a')
# print("Q5",a)
# #=========================================================================
# # 반환하는 메서드 (return methods)
# #2-2. 리스트 a를 오름차순으로 정렬 > 원본을 변경하지 않는다.
# print(sorted(a))
# print(a)
# #6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 반환값 출력 ★★★★★ > stack(후입선출), popleft 메서드 queue(선입선출)
# print(a.pop())
# #7. 리스트 a에서 문자 'n'의 개수 출력
# print(a.count('n'))


#------------------------------------------------------------------------------------

# 복사 part
#1. 할당

# list1 = [1,2,3,4]
# list2 = list1
# print(id(list1),id(list2))
# list2[0]=5
# print(list1, list2)

#2. 얕은 복사
# list1 = [1,2,3,[4,[5,6]]]
# list2 = list1.copy()
# print(id(list1)==id(list2))
# print(id(list1[3])==id(list2[3]))
# list2[3][0] =555
# print(list1, list2)
# print(id(list1[3][1][0])==id(list2[3][1][0])) # [5,6]의 5 주소는 같다

#3. 깊은 복사
# import copy
# list1 = [1,2,[3,4]]
# list2 = copy.deepcopy(list1)
# print(id(list1),id(list2))
# print(id(list1[2]),id(list2[2]))

#--------------------------------------

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # code .....

    print(f'{tc} {result}')