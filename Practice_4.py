star = int(input("숫자를 입력하세요"))


for i in range(0,star):
    print(' ' * i,end='')
    print('*' * ((star-i) * 2 - 1))

for i in range(1,star):
    print(' ' * (star-1-i),end='')
    print('*' * ((i + 1)*2 -1) )


# print(' ' * 0,end='')
# print('*' * 9)

# print(' ' * 1,end='')
# print('*' * 7)

# print(' ' * 2,end='')
# print('*' * 5)

# print(' ' * 3,end='')
# print('*' * 3)

# print(' ' * 4,end='')
# print('*' * 1)


#     1,3,5,7,9,11
# ********* 9 ,0
#  *******  7, 1
#   *****   5, 2
#    ***    3, 3
#     *     1, 4
#    ***
#   *****
#  *******
# *********