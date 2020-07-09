# a = 2**8
# print(a)

# "hello" + "world"

# a = "hello"
# print(a[:])
# print(a[0:])

# t = a.count('l')
# print(t)

# a = "hellO"
# print(a*3)

# print(a[0])

# ab = 180
# b = "광주인공지능 학생수 %d" %ab #
# print(b) 

# ### 
# a = 123
# c = '안녕'

# b = f'광주인공지능사관학교 학생수 {a},{c}'
# print(b)

# b = f'광주 인공지능사관학교 {a},{c}'
# a = [2,3,4,5]
# print(a.index(4))

# a = {'name':'line','age':20}
# print(a['name'])
# print(a['age'])
# print(a.keys())
# print(a.values())
# print(a.items())

# while(count<4):
#     count = count +1
#     print("출력")

# if i == 2:
#     pass


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('팻 생성완료')

#     def eat(self, food):
#         print(f'{food}를 먹었습니다.')

# class Dog:
    


# dog = Pet('강아지', 3)


# print(dog.name)
# print(dog.age)
# print(dog.eat("밥"))


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def Area(self):
        return self.width * self.height

    def Rod(self):
        return 2 * (self.width + self.height)

ret_1 = Rect(10,20)
print(ret_1.Area())
print(ret_1.Rod())



class Anim:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('펫생성')

    def eat(self,food):
        print(f'{food}를 먹었습니다.')

class Dog(Anim):
    def Howl():
        print("멍멍")

class Cat(Anim):
    def Howl():
        print("야옹")

dog_1 = Dog()
dog_1.Howl()

cat_1 = Cat()
cat_1.Howl()