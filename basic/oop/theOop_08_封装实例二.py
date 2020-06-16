class Gun:
    """枪类"""

    def __init__(self, model):
        # 1. 枪的型号
        self.model = model

        # 2. 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        """装填子弹"""
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return

        # 发射子弹
        self.bullet_count -= 1

        # 提示发射信息
        print("[%s] 突突突... [%d]" % (self.model, self.bullet_count))


class Soldier:
    """士兵类"""

    def __init__(self, name):
        self.name = name

        # 枪 - 新兵没有枪
        self.gun = None

    def fire(self):
        # 判断士兵是否有枪
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)
            return

        # 高喊口号
        print("冲啊...[%s]" % self.name)

        # 让枪装填子弹
        self.gun.add_bullet(50)

        # 让枪发射子弹
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")

# 创建士兵
soldier1 = Soldier("士兵一号")
soldier2 = Soldier("士兵二号")

soldier1.gun = ak47
soldier1.fire()
soldier2.fire()

print(soldier1.gun)
print(soldier2.gun)  # 结果为None >> python中没有NPE
