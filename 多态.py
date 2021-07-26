# 多态成立的三个条件：
# 1.有继承
# 2.有方法的重写
# 3.有父类或子类对象作为参数
class Dog:
    def __init__(self,name):
        self.name =name

    def game(self):
        print("普通狗再地上玩耍")
class Xiao_tian_quan(Dog):
    def __init__(self,name):
        self.name =name
    def game(self):
        print(" % s可以再天上飞快玩耍"% self.name)
class Person:
    def __init__(self,name):
        self.name = name
    def play_with_dog(self,dog):
        print("人物：%s 和狗对象：%s 一起玩耍"%(self.name,dog.name))
        dog.game()
# 由普通狗创建对象
wang_cai = Dog("旺财")
# 人类模板创建对象
chang_wei = Person("常威")
# 调用和狗玩的对象
chang_wei.play_with_dog(wang_cai)
print("_"*40)
XTQ = Xiao_tian_quan("哮天犬")
chang_wei.play_with_dog(XTQ)