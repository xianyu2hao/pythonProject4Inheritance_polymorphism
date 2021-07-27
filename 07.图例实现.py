# 设计一个game类
# 1.设计属性：定义一个类属性top_score记录游戏的历史最高分；定义一个实例属性play_name记录当前游戏玩家姓名。
# 2.设计方法：类方法show_top_score显示最高分；静态方法show_help显示游戏帮助信息；实例方法start_game开始当前玩家游戏。
# 3.主要程序步骤：1）查看帮助信息；2）查看历史最高分；3）创建游戏对象，开始游戏
class Game:
    """游戏类"""
    # 类属性,记录游戏的历史最高分
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod
    def show_help():
        """静态方法"""
        print("显示游戏帮助信息：小样！加油吧，你可以的！")
    @classmethod
    def  show_top_score(cls):
        """类方法"""
        print("显示历史最高分：",cls.top_score)
    def start_game(self):
        """实例方法"""
        print("游戏开始！Go!")
        print("%s玩家玩的很Happy！"% self.player_name)
        # 修改历史最高分
        Game.top_score += 100
# 调用函数
Game.show_help()
Game.show_top_score()
# 创建对象，开始游戏
xiao_zhang = Game("小张")
xiao_zhang.start_game()
Game.show_top_score()