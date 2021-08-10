'''
    任务：
        优化购物小条
        10机械革命优惠券，0.5
        20张卫龙辣条优惠券 0.3
        15张HUA WEI WATCH 0.8
        随机抽取一张优惠券。


    商城：
        1.准备一些商品
        2.有空的购物车
        3.钱包
        4.结算
    流程：
        看你输入的产品存不存在，
            若存在
                若钱够了：
                    将商品添加到购物车
                    钱包余额减去商品的钱
                若钱不够
                    温馨：
            若不存在
                温馨提示：
            非法输入：
        退出：
            打印购物小条
'''
import copy
import random
import time

b = 1  # 机械革命
c = 1  # HUA WEI WATCH
d = 1  # 卫龙辣条

shop = [
    ["lenovo PC", 5600],
    ["HUA WEI WATCH", 1200],
    ["Mac pro", 12000],
    ["洗衣机", 3000],
    ["机械革命", 5000],
    ["卫龙辣条", 4.5],
    ["老干妈辣酱", 20],
]

a = random.randint(0, 44)

# 1.准备好钱包

money = input("亲输入您的初始余额：")
money = int(money)
ticket = input("您是否要抽取优惠券？\n y/n?\n")
if ticket == "y":
    # time.sleep(2)
    if a >= 0 and a <= 9:
        b = 0.5
        shop[4][1] = round(shop[4][1] * b, 2)

        print("恭喜您抽中一张机械革命五折优惠券")
    elif a > 9 and a <= 29:
        d = 0.3
        shop[5][1] = round(shop[5][1] * d, 2)
        print("恭喜你抽中一张卫龙辣条三折优惠券")
    elif a > 29 and a <= 44:
        c = 0.8
        shop[1][1] = round(shop[1][1] * c, 2)
        print("恭喜您抽中一张HUA WEI WATCH八折优惠券")
else:
    pass

# 2. 准备一个空的购物车
mycart = []

sum = 0
# 3.开始购物
sum = 0
i = 0
while i < 20:
    for key, value in enumerate(shop):
        print(key, value)
        # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")

    if chose.isdigit():
        chose = int(chose)  # "1" --> 1
        if chose > len(shop) or chose < 0:  # 9 > 7
            print("该商品不存在！别瞎弄！")
        else:
            if money >= shop[chose][1]:
                money = money - shop[chose][1]
                mycart.append(copy.deepcopy(shop[chose]))
                sum = sum + shop[chose][1]
                print("恭喜，商品添加成功！您的余额为：￥", money)
                if b != 1 and chose == 4:
                    shop[4][1] = 5000
                elif c != 1 and chose == 1:
                    shop[1][1] = 1200
                elif d != 1 and chose == 5:
                    shop[5][1] = 4.5
