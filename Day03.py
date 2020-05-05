#分支結構
"""
if and else的運用
使用者帳號跟密碼登入
帳號為admin、密碼為123456才可登入
"""

username = input("請輸入帳號名稱：")
passward = input("請輸入密碼：")
if username == 'admin' and passward == '123456':
    print("帳號密碼正確，登入成功")
else:
    print("驗證失敗，請再輸入一次")

#多分支結構
"""
if, elif, and else運用
f(x) = 3x + 4 (x>1)
       2x + 3 (-1 >= x >= 1)
        x - 2 (x < -1)
"""

x = float(input("請輸入x的數值："))
if x > 1:
    y = 3 * x + 4
elif x >= -1:
    y = 2 * x + 3
else:
    y = x -2
print( 'f( %.2f) = %.2f' % ( x , y ))


#練習
"""
英制單位英吋與公制單位公分互換。
1 inch = 2.54 cm
"""


value = float(input("請輸入長度："))
unit = input("請輸入單位：")
if unit == "in" or unit == "英吋" or unit == "inch":
    print ('%.2f英吋 = %.2f公分' %(value, value * 2.54))
elif unit == "cm" or unit == "公分" or unit == "釐米":
    print ('%.2f公分 = %.2f英吋' %(value, value / 2.54))
else:
    print("請輸入正確的單位")


#練習：百分製成績轉換為等級製成績。
"""
百分製成績轉換為等級製成績
90~100  A
80~90   B
70~80   C
60~70   D
<60     E
"""


score = float (input("請輸入成績："))
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else:
    grade = 'E'
print('對應的等級：', grade)


#練習：輸入三條邊長，如果能構成三角形就計算周長和面積。
a = float(input("請輸入第一個數字："))
b = float(input("請輸入第二個數字："))
c = float(input("請輸入第三個數字："))
if a + b > c and a + c > b and b + c > a :
    peri = a + b + c
    s = peri / 2
    area = (s * (s - a)* (s - b)* (s - c)) ** (1/2)
    print("三角形周長：%.2f" % peri)
    print("三角形面積：%.2f" % area)
else:
    print("無法組成三角形")