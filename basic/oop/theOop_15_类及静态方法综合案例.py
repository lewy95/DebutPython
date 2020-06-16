class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


# 查看游戏的帮助信息：调用静态方法
Game.show_help()

# 查看历史最高分：调用类方法，类方法中调用了类属性
Game.show_top_score()

# 创建游戏对象：调用实例方法
game = Game("yy")
game.start_game()
