zero = 0
one = 0
counting = [0,0]

def fibonaccie(n):
    if n == 0:
        global zero
        zero = zero + 1
        global counting 
        counting.append()
        return 0
    elif n == 1 :
        global one
        one = one + 1
        return 1
    else:
        return fibonaccie(n-1) + fibonaccie(n-2)


print(fibonaccie(6))
print('0이 Return 된 횟수 : ' ,zero)
print('1이 Return 된 횟수 : ' ,one)