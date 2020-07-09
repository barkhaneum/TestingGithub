class Anim:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('펫생성')

    def eat(self,food):
        print(f'{food}를 먹었습니다.')

class Dog(Anim):
    def Howl(self):
        print("멍멍")

class Cat(Anim):
    def Howl(self):
        print("야옹")

dog_1 = Dog('해피',2)
dog_1.Howl()

cat_1 = Cat('야옹이',3)
cat_1.Howl()