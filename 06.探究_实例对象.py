class Person(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s爱吃美食"% self.name)

xiao_ming =Person("小明") # 由类创建的对象在内存空间中实际存在，故称为 实例对象
print(xiao_ming)  # 其属性称为 实例属性
print(xiao_ming.name)
xiao_ming.eat() # 其方法成为 实例方法