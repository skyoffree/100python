##整數
#二進制(0b)、八進制(0o)、十六進制(0x)
print("二進制的數：",0b100) 
print("八進制的數：",0o100) 
print("十六進制的數：",0x100) 
##浮點數
#支援科學技數法 e2= 10^2
print("使用科學技數法(1.2345e2)=",1.2345e2)

##使用變量進行加減乘除
a = 123
b = 45
print("兩數的四則運算:",a,"跟",b)
print("加法:", a + b) 
print("減法:", a - b)
print("乘法:", a * b)
print("除法:", a / b)

##使用type()檢查變量的類型
a = 10
b = 1.23
c = 1 +2j
d = 'hello, world'
e = True
print("""a = 10
b = 1.23
c = 1 +2j
d = 'hello, world'
e = True""")
print('a的類型是：',type(a))
print('b的類型是：',type(b))
print('c的類型是：',type(c))
print('d的類型是：',type(d))
print('e的類型是：',type(e))

##類型轉換
"""
int()  ：將一個數值或字符串轉換成整數，可以指定進制。
float()：將一個字符串轉換成浮點數。
str()  ：將指定的對象轉換成字符串形式，可以指定編碼。
"""

##使用者輸入數字，並進行運算
# %d 整數佔位符號、 %f 小數佔位符號
a  =  int ( input ( 'a = ' ))
b  =  int ( input ( 'b = ' ))
print ( '%d + %d = %d'  % ( a , b , a  +  b ))
print ( '%d - %d = %d'  % ( a , b , a  -  b ))
print ( '%d * %d = %d'  % ( a , b, a * b ))
print ( '%d / %d = %f'  % ( a , b , a / b ))
print ( '%d // %d = %d'  % ( a , b , a // b ))
print ( '%d %% %d = %d'  % ( a , b , a % b ))
print ( '%d ** %d = %d'  % ( a , b , a ** b ))

##複合運算符號 
a = 10
b = 2
print("a的數值:", a)
a += b #相當於a = a+b
print("a+b的數值:", a)
a *= a+1 #相當於a = a*(a+1)
print("a*(a+1)的數值:", a)

#比較運算符和邏輯運算符
"""
True and True = True
True and False = False 
False and True = False 當左邊是False，則右邊不執行
and 左右兩邊都是True才會是 True
or 左右兩邊只要有一個是True，就會是True
"""

##比較運算符和邏輯運算符的使用
flag0  =  1  ==  1 
flag1  =  3  >  2 
flag2  =  2  <  1 
flag3  =  flag1  and  flag2 
flag4  =  flag1  or  flag2 
flag5  =  not ( 1  !=  2 )
print ( 'flag0 =' , flag0 )     # flag0 = True 
print ( 'flag1 =' , flag1 )     # flag1 = True 
print ( 'flag2 =' , flag2 )     # flag2 = False 
print ( 'flag3 =' , flag3 )     # flag3 = False 
print ( 'flag4 =' , flag4 )     # flag4 = True 
print ( 'flag5 =' , flag5 )     # flag5 = False

#練習1 華氏溫度轉換為攝氏溫度
#公式為  C = (F - 32)/1.8
f = float(input("請輸入華氏溫度:"))
c = (f - 32) / 1.8
print('%.1f華氏溫度=%.1f攝氏溫度' %(f,c))

#練習2：輸入圓的半徑計算計算周長和麵積。
radius = float (input("請輸入圓的半徑: "))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * (radius ** 2)
print( '周長:%.2f' % perimeter)
print( '面積:%.2f' % area)

#練習3：輸入年份判斷是否為閏年。
#閏年輸出True，否則輸出False
#4的倍數 ，但100的倍數不是閏年，但遇到400的倍數會是閏年。 
year = int(input("請輸入年分："))
leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(leap_year)