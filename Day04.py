#用for迴圈求1+2+3...+100

sum = 0
for count in range(101):
    sum += count #sum = sum + count  
print(sum)

#用for迴圈求1~100的偶數合
#method 1
sum = 0
for count in range(0,101,2):
    sum += count #sum = sum + count  
print(sum)
#method 2
sum = 0
for count in range(101):
    if count % 2 == 0:
        sum += count #sum = sum + count  
print(sum)

#猜數字遊戲
import random
answer = random.randint(1,100)
counter = 0
while True:
    counter +=1
    number = int (input("請輸入數字:"))
    if number < answer:
        print ("再大一點")
    elif number > answer:
        print ("再小一點")
    else:
        print ("恭喜你答對啦")
        break
print("你總共猜了%d 次" % counter)
if counter > 7 :
    print("你可以再想更好的猜法")

#輸出九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = %d' %(i,j,i*j), end='\t')
    print()

#練習1：輸入一個正整數判斷是不是質數。
#提示：質數指的是只能被1和自身整除的大於1的整數。
from math import sqrt

num = int (input( "請輸入一個正整數："))
end = int (sqrt(num))
is_prime = True
for x in range(2, end +1):
    if num % x == 0 :
        is_prime = False
        break
if is_prime and num != 1:
    print( "%d是質數" % num)
else:
    print( "%d不是質數" %num)

#練習：輸入兩個正整數，計算它們的最大公約數和最小公倍數。
a = int(input('a='))
b = int(input('b='))
#IF a> b 交換 a和b的值
if a > b:
    a , b = b , a 
#從兩個數較小的數開始遞減循環
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print("%d和%d的最大公約數是%d" %(a,b,factor))
        print("%d和%d的最小公倍數是%d" %(a,b,a * b // factor))
        break


#練習3：輸出指定的三角形圖案。
"""
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""


row  =  int ( input ( '請輸入行數: ' ))
for  i  in  range ( row ):
    for  _  in  range ( i  +  1 ):
        print ( '*' , end = '' )
    print ()

row  =  int ( input ( '請輸入行數: ' ))
for  i  in  range ( row ):
    for  j  in  range ( row ):
        if  j  <  row  -  i  -  1 :
            print ( ' ' , end = '' )
        else :
            print ( '*' , end = '' )
    print ( )

row  =  int ( input ( '請輸入行數: ' ))
for  i  in  range ( row ):
    for  _  in  range ( row  -  i  -  1 ):
        print ( ' ' , end = '' )
    for  _  in  range ( 2  *  i  +  1 ):
        print ( '*' , end = '' )
    print ()
