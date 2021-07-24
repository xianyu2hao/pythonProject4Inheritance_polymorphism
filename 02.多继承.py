# 定义爷爷类
class Animal:
    def __init__(self):
        """初始化方法"""
        self.name = "动物"
        self.age = 2

    def eat(self):
        print(
            "% s都爱吃鱼" % self.name
        )


# 定义父亲类
class Cat(Animal):
    "猫类"

    def catch(self):
        """抓方法"""
        print("小猫抓老鼠")


# 定义孙子类
class Bosimao(Cat):
    """波斯猫类"""

    def sing(self):
        print("波斯猫可以唱歌")


# 使用孙子类模板创建对象
BSM = Bosimao()
BSM.sing()
BSM.catch()
BSM.eat()
print(BSM.name)
# 孙子类可以访问爷爷类和父亲类的对象和方法


# 使用爷爷类模板创建对象
ANM = Animal()
# ANM.Catch 爷爷类对象不能调用子类的属性，同样不能调用孙子类属性
