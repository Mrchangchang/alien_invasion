class GameStats():
    """ 跟踪游戏的统计信息 """
    def __init__(self, ai_setting):
        """ 初始化统计信息 """
        self.ai_setting = ai_setting
        # 再任何情况下都不应该重置最高得分 
        self.high_score = 0
        self.reset_stats()
        # 游戏启动时处于活动状态
        self.game_active = False
    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1