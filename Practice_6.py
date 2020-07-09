import numpy as np
arr1 = np.array([1,2,3])
print(arr1)

arr1 = np.arange(0,10,2)
print(arr1)

arr1 = np.arange(0,10)
print(len(arr1))
print(arr1.size) #리스트에서는 지원하지 않는 기능

arr1 = np.linspace(0,20,4) #0~20까지를 4개로 나눠서 범위를 출력해준다.

arr1 = np.ones((2,3)) #내가 원하는 ..??
print(arr1)

arr1 = np.array([1,2,True,False]) #전부다 숫자로 출력해버린다.
print(arr1)

arr1 = np.array([1,2,True,'안녕']) #전부다 문자로 변해버린다.
print(arr1)

arr1 = np.array([1,2,3],[4,5,6])
print(arr1[0])
print(arr1[0,2])

arr1 = np.array([1,2,3],[4,5,6])
print(arr1[1:,1:])

arr1 = np.array([[1,2,3],[7,8,9]])
print(arr1[1:,1:])

arr1 = np.array([1,2,3],[4,5,6])
print(arr1.ndim)
print(arr1.shape())

arr1 = np.arange(20)
print(arr1.reshape(-1,1)) # -1은 뒤집는다라는 의미로써 이해하면됨
#정확한 의미는 내가 직접 찾아보도록 하자

arr1 = np.arange(20)
print(arr1)
print(arr1.reshape(20,1))
print(arr1.reshape(-1,1))

arr1 = np.arange(30)
arrMask = ((arr1 % 3 ) == 0)
print(arr1[arrMask])

arr1 = arr1.array([[2,2],[3,4]])
arr2 = np.append(arr1, [[3,3]], axis = 0) #행으로 행렬을 붙여준다.
arr3 = np.append(arr1, [[3],[3]], axis = 1) #열로 행렬을 붙여준다.

print(arr2)

arr1 = np.array([1,2,3],[4,5,6])
abb = np.delete(arr1,0, axis =0) #행을 삭제시키려면 axis = 0 ,열은 axis = 1
print(abb)

arr1 = np.array([1,2,3],[4,5,6])
abb = np.delete(arr1,(2,4)) #비항구조적?? 무슨말이지
print(abb)

arr1 = [[1,2,3],[4,5,6]]
arr4 = np.delete(arr1, 0)
print(arr4)

arr1 = [[1,2,3],[4,5,6]]
arr = np.delete(arr1,(0,2,4))
print(arr4)


