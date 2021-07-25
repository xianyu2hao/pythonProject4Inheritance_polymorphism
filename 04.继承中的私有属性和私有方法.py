
class Father:
    """父类"""
    def __init__(self):
        "初始化方法"
        self.name = "老王"
        self.__password = 123456 #私有属性
    # 类的内部提供对外接口 get/set
    def get_pwd(self):
        """获取私有属性"""
        return self.__password
    def set_pwd(self,new_password):
        "设置私有属性"
        self.__password = new_password
    def fun_secret(self):
        """调用私有方法"""
        return self.__secret()
    def eat(self):
        """吃方法"""
        print("%s喜欢吃东西"% self.name)
    def __secret(self):
        """私有方法"""
        print("%s的银行卡密码是：%d"%(self.name,self.__password))
class Son(Father):
    """子类"""
    def run(self):
        print("小王喜欢跑来跑去")
# 子类创建对象
xiao_wang =Son()
print(xiao_wang.name)
# 类外子类无法访问父类的私有属性和私有方法
# print(xiao_wang.pssword)
# xiao_wang.__secret()
xiao_wang.eat()
#调用
print(xiao_wang.get_pwd())
xiao_wang.set_pwd(1008636)
print(xiao_wang.get_pwd())

xiao_wang.fun_secret()
