# 覆盖和拓展
# 子类中有与父类相同的方法名，子类重写了父类的方法
# 父类不能满足子类的需求。重写的前体是有继承关系
# 分别：功能覆盖和功能拓展两种
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
    def  catch(self):
        """抓方法"""
        print("波斯猫喜欢抓小鱼")
        # 功能扩展，在子类重写方法中，调用父类的方法。格式：super().重写方法名()
        super(Bosimao, self).catch()
        # 功能扩展,方法2格式：父类名.方法名（self）,不推荐使用,方法名改了，就错误。
        # Cat.catch(self)
    def sing(self):
        print("波斯猫可以唱歌")


BSM = Bosimao()
BSM.catch()
# 这里进行抓方法运用的是自己的子类的，直接覆盖了父类的抓方法功能