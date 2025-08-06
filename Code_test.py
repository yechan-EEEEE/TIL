#print("Hello World")
#print(-2 ** 4)

# -(2 ** 4)

# (-2) ** 4
# number = 10
# double = 2 * number
# print(double)
# number = 5
# double = 2 * number
# print(double)
# print = 'Hello World'
# print[print]

# 1 = range(0, 10, 0)
# print(1)
# '''
# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print('hello'.capitalize())
# text = 'banana'
# print(text.find('x'))
# print(text.index('x'))  
# my_list=[3,2,100,1]
# my_list.sort(reverse=False)
# print(my_list)
# data = [1,2,3,4,5]
# cnt = 0
# def custom_len(items):
#     for i in items:
#         cnt += 1
#     return
# print(custom_len(data))
# def custom_max(items):
#     #리스트에서 가장 큰 값을 찾아 반환
#     max_value = items[0]#첫번째 값이 가장 크다

#     for item in items[1:]:#첫번째를 제외하고 나머지 애들을 순회
#         if max_value < item:#현재 최대값보다 지금 접근하는 값이 더 크면
#             max_value = item#새로운 최대값이 나왔으니 갱신
#     return max_value
# print(custom_max(data))
# def custom_sum(items):
#     total = 0
#     for item in items:
#         total += item
#     return total
# print(custom_sum(data))
# def custom_index(items, value):
#     for item in items:
#         if item == value:
# a = 1
# b = 2
# def enclosed():
#     a = 10
#     c = 3
#     def local(c):
#         print(a,b,c) 
#     local(500)
#     print(a,b,c) #10,2,500
# enclosed() # 10,2,3
# print(a,b) # 1,2
# num = 0
# def increment():
#     global num
#     num += 1
# print(num)
# increment()
# print(num)
# a  = 20
# b=a
# b=10
# print(a)
# print(b)
# print(a is b)
# my_set = {'a','b','c',1,2,3}
# element = my_set.pop()
# print(element)
# print(my_set)
# data = [1, 2, 3, 4, 5]
# def custom_len(items):
#   # 리스트의 요소 개수를 세어 반환
#   cnt = 0  # 처음에는 0개 ,, 이후 순회하면서 이 친구를 증가시킬 거다. 
#   for _ in items:  # 순회한 횟수만큼 cnt를 1씩 더해준다. 
#     # cnt += 1
#     cnt = cnt + 1
#   return cnt  # 센 숫자를 반환해야 한다. 

# print(custom_len(data)) #5
# # max() 함수 => 리스트에서 최대값을 구하는 함수 


# def custom_max(items):
#   # 리스트에서 가장 큰 값을 찾아 반환
#   max_value = items[0]  # 지금은 첫 번째 값이 가장 크다.

#   for item in items[1:]:  # 첫 번째를 제외하고, 나머지 애들을 순회 
#     # 왜 순회를 하죠 ? 최대값을 구하려고...
#     # 현재 최대값은 max_value에 저장되어 있다. 
#     if max_value < item:  # 현재 최대값보다 지금 접근하는 값이 더 크면!
#       max_value = item  # 새로운 최대값이 나왔기 때문에 갱신해야죠.. 최대값을 
  
#   return max_value
# print(custom_max(data))

# # min() 함수
# def custom_min(items):
#   # 리스트에서 가장 작은 값을 찾아 반환
#   min_value = items[0]
#   for item in items[1:]:
#     if item < min_value:
#       min_value = item

#   return min_value
# print(custom_min(data))

# # sum() 함수
# # 주어진 리스트에 있는 모든 값을 합하는 것 
# def custom_sum(items):
#   # 리스트의 모든 요소를 더한 값을 반환
#   total = 0
#   for item in items:
#     total += item 
  
#   return total
# L = [10, 20, 30, 20, 40]
# print(custom_sum(data))
# # index() 함수
# def custom_index(items, value):
#     # 리스트에서 특정 값(value)의 첫 위치를 찾아 반환
#     # 원래는 아니지만 못 찾으면 -1을 반환하도록 구현 
#     # enumerate
#     for idx, item in enumerate(items):  # 쭉 리스트를 순회합니다. 
#        if item == value:  # 내가 찾으려는 값과 지금 순회중인 값이 같으면, 그 친구의 인덱스를 반환!!!
#           return idx  # return : 함수의 반환, 끝... 
       
#     return -1

# print(custom_index(L, 30))

# # count() 함수
# def custom_count(items, value):
#     # 리스트에 특정 값(value)이 몇 개 있는지 세어 반환
#     cnt = 0
#     for item in items:
#         if item == value:
#             cnt += 1 # 값이 같을 때마다 카운트 증가
#     return cnt
# print(custom_count(data,1))

# # reverse() 함수
# # 역순 ,,,   [1, 10, 5, 7, 2]  => [2, 7, 5, 10, 1]
# # reverse 한 새로운 결과를 반환하자. 
# def custom_reverse_new(items):
#     new_list = []
#     # for문을 뒤에서부터 돌려보자. 

#     for i in range(len(items) - 1 , -1, -1):
#         new_list.append(items[i])
#     return new_list
# print(custom_reverse_new(data))
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         print(numbers[j][i], end=' ')
#         '''
#         0 0 1
#         1 0 4
#         2 0 7
#         0 1 2
#         1 1 5
#         2 1 8
#         0 2 3
#         1 2 6
#         2 2 9
#         '''
# print()
# class Animal:
#  def __init__(self, name):
#     self.name = name

#  def walk(self):
#     print('걷는다!')

#  def eat(self):
#     print(f'{self.name}!먹는다!')

# dog = Animal('dog')
# dog.walk()
# lunch = ['짜장면', '짬뽕', '탕수육']
# for idx, num in enumerate(lunch):
#     print(idx, num)
#     # 아래는 출력 예시입니다.
#     # 0 짜장면
#     # 1 짬뽕
#     # 2 탕수육
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# T = int(input())
# for test_case in range(1, T + 1): # 1부터 T만큼 돌기
#     x = int(input())
#     a = list(map(int,input().split()))
#     # a = [들온 애들 순서대로 드가있음]
#     max_num = a[0]
#     min_num = a[0]
#
#     for n in a:
#         if n > max_num:
#             max_num = n
#         if n < a:
#             min_num = n
#     Answer = max_num - min_num
#     print(f"#{test_case} {Answer}")
