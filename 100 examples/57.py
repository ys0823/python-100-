#----------------------------------------------
#809??=800??+9??+1 其中??代表的两位数,
# 8??的结果为两位数，9??的结果为3位数。
# 求??代表的两位数，及809??后的结果。
#2018-8-20
#----------------------------------------------
'''
a = 809
for i in range(10,100):
    c = 900+i
    a = 80900+i
    b = 80000+i
    if a == b+c+1:
        print('%d = %d+%d+%d'%(a,b,c,d))
'''
a = 809
for i in range(10,100):
    b = i*a+1
    if b >=1000 and b<= 10000 and 8*i < 100 and 9*i >=100:
        print(b, '/' , i,'=800 * ' ,i,'+9*',i,'+' ,b % i)
        print(i)