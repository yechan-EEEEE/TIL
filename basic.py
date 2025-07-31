# #print("Hello World")
# '''
# -2 ** 4

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
data = [1,2,3,4,5]
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
def custom_sum(items):
    total = 0
    for item in items:
        total += item
    return total
print(custom_sum(data))
# def custom_index(items, value):
#     for item in items:
#         if item == value:
