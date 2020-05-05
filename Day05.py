
#尋找所有水仙花數
"""
說明：水仙花數也被稱為超完全數字不變數、自戀數、自冪數、阿姆斯特朗數，
它是一個3位數，該數字每個位上數字的立方之和正好等於它本身，
例如： 1^3 + 5^3+ 3^3=153。
"""
"""
思路
Step1.定義範圍 Range(100,1000)
Step2.拆解個位數(c)、十位數(b)、百位數(a)
Setp3.設定方程式 a^3 + b^3 + c^3 = a*100 + b*10 + c*1
"""

for num in range(100,1000,1):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


#正整數的反轉
"""
例如12345經過程式後變為54321
"""
"""
思路
Step1.使用者輸入正整數
Step2.定義反轉數=0
Step3.正整數除以10取餘數，放入反轉數
Step4.
使用while迴圈，當正整數大於零，則反轉數 = 反轉數*10 + 正整數除以10的餘數
"""
num = int(input('請輸入正整數：'))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num *10 + num % 10
    print(reverse_num,num)
    num //= 10
    print(num)
print(reverse_num)

#百元百雞
"""
公雞一隻5元、母雞一隻3元、小雞三隻一元
用一百元買一百隻雞，請問公雞、母雞、小雞各幾隻
"""

"""
思路
step1. 聯立方程式
       5a + 3b + c/3 = 100
        a + b + c = 100
step2. a的範圍為0~20 (用range)
       b的範圍為0~33 (用range)
step3. c可寫為 100 - a - b
step4 當 5a + 3b + c/3 == 100時，就是答案
"""
for a in range(0,20):
    for b in range(0,33):
        c = 100 - a - b
        if 5 * a + 3 * b + c / 3 == 100:
            print("公雞：%d隻,母雞：%d隻,小雞：%d隻" %(a,b,c))

#CRAPS賭博遊戲
"""
玩家第一次搖骰子如果搖出了7點或11點，玩家勝；
玩家第一次如果搖出2點、3點或12點，莊家勝；
其他點數玩家繼續搖骰子，如果玩家搖出了7點，
莊家勝；如果玩家搖出了第一次搖的點數，
玩家勝；其他點數，玩家繼續要骰子，直到分出勝負。
"""

"""
設定玩家開始遊戲時有1000元
遊戲結束條件是玩家輸光所有賭注
"""
from random import randint
money = 1000
while money > 0 :
    print("你的總資產：", money)
    needs_go_on = False
    while True:
        debt = int (input ("請下注："))
        if 0 < debt <= money:
            break
    first = randint(1,6 ) + randint(1,6)
    print("玩家搖出%d點" %first)
    if first == 7 or first == 11:
        print("玩家勝！")
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print("莊家勝！")
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on :
        needs_go_on = False
        current = randint(1,6) + randint(1,6)
        print("玩家搖出了%d點" %current)
        if current == 7:
            print('莊家勝')
            money -= debt
        elif current == first:
            print('玩家勝')
            money += debt
        else:
            needs_go_on = True
print("你破產了，遊戲結束")

#練習:生成斐波那契數列的前20個數。
"""
斐波那契數列的特點是數列的前兩個數都是1，從第三個數開始，
每個數都是它前面兩個數的和，形如：1, 1, 2, 3, 5 , 8, 13, 21, 34, 55, 89, 144
"""

"""
思路
step1. 定義數學式 A(n) + A(n+1) = A(n+2)
step2. A(n) = 1, A(n+1) = 1
step3. for 迴圈進行20次
step4. print A(n+2)
"""

count = 0
An = 1
An2 = 1
print(An)
print(An2)
while count < 18: 
    count = count + 1
    Anew = An + An2
    An = An2
    An2 = Anew
    print(Anew)
    continue

#練習：找出10000以內的完美數。
"""
所有的真因子（即除了自身以外的因子）的和（即因子函數）恰好等於它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美數。
"""

import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)

#輸出100以內所有的質數。
from math import sqrt

for num in range(2, 101):
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end+1): 
        if num % x == 0 :
            is_prime = False
            break
    if is_prime and num != 1:
        print(num)