# 一个子类和一个父类称为单继承
#定义父类
class Animal:
    """动物类"""
    def __init__(self):
        self.name = "家养动物"
        self.age = 2
    def eat(self):
        print("%s都喜欢吃" % self.name)

class Cat(Animal):
    """猫类"""
    def cat(self):
        print("小猫抓老鼠")

# 使用父类模板创建对象
animal = Animal()
print(animal.name)
# 父类对象无法调用子类的方法
# animal.catch()
print("_"*45)

# 使用子类模板创建对象
tom = Cat()
print(tom.name)
print(tom.age)
tom.eat()
# 子类可以使用父类的属性
# 继承不是复制
# 访问子类属性时，先到子类查找，子类中没有找父类