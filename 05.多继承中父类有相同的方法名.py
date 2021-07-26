# 多继承中，父类有相同的方法名，调用顺序
# 例如骡子是驴和马的后代；骡子mule,马horse，驴donkey
class Horse:
    def run(self):
        print("跑得快")

    def walk(self):
        print("走不远")
class Donkey:
    def walk(self):
        print("走得远")
    def run(self):
        print("跑不快")

class Mule(Horse,Donkey):
    pass

mu = Mule()
mu.walk()
mu.run()

# 方法解析顺序__mro__，格式：类名.__mro__
print(Mule.__mro__)