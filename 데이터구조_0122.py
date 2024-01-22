# help(str)
# print(help(list))

# def append():
#     print("5")
#     pass
# append()

# # 문자열 메서드
# print('hello'.capitalize()) #Hello

# s = 'k1235k'
# print(s.isalpha())


# my_str = 'banana'
# # find, index
# print(f"{my_str.find('b')} : find b")
# print(f"{my_str.index('a')} : index a")

# # isalpha
# string1='Hello'
# string2= '123'
# string3='12a3'
# print(f"{string1.isalpha()} : isalpha") #True
# print(f"{string2.isalpha()} : isalpha") #False
# print(f"{string3.isalpha()} : isalpha") #False

# 문자열 조작 메서드
# sen1='my name is blaaaa my code is hahaha'
# num1=int(input())
# new_sen1=sen1.replace('my','your',num1)
# print(new_sen1)
# text = 'Hello, world!'
# new_text = text.strip('l') # 처음과 끝이 아니므로 l이 제거되지않음
# print(new_text)

# text = 'Hello, wo    rld!'
# words = text.split()
# print(words)

# words_test = '-'.join(words)
# print(words_test)

# a = input().split()
# print(a)

# 리스트 값 추가
my_list = [11,22,33,22]

# # append
# my_list.append(4)
# (my_list.append([5,4,3]))
# print(my_list)
# my_list.extend([7,6,5])
# print(my_list)

# my_list.insert(2,'ssafy')

# print(my_list)
# print(my_list.pop())
# print(my_list)

# my_sen = 'My name is Baeeeeeeeksseungwwwwwo'
# index = my_sen.index('')
# print(index)
# count_num = my_sen.count('e')
# print(count_num)
# my_list = [1,4,5,87,6]
# my_list.sort(reverse=True)
# print(my_list)

# 얕은 복사
# a = [1,2,3]
# b = a[:]
# print(b)
# b[0]= 100
# print(f'b는 {b}, a는 {a}')
# a = [1,2, [100,200]]
# b = a[:]
# print(b)
# b[2][0] = 9999
# print(b)
# print(a)

# import copy
# original_list = [1,2,[100,[5,55,555],200]]
# deep_copied_list = copy.deepcopy(original_list)
# # deep_copied_list = original_list[:] # 이게 얕은 복사
# deep_copied_list[2][1][1] = -1

# print(original_list)
# print(deep_copied_list)

# a='32'
# b=3.5
# print(a.isnumeric())

# print('hello'.capitalize()) #Hello
# 온라인 강의는 여기까지 ------------------


