#------------------------------------
#问题简述：一只小猴子吃桃子的问题。
#话说，一只小猴子第一天摘下若干个桃子，并吃了一半。感觉到吃的还不瘾，于是又多吃了一个
#第二天早上，又将剩下的桃子吃掉一半，又多吃了一个。
#以后每天早上,都吃了前一天剩下的一半零一个。
#问题：请问，到了第10天早上想再吃时，却发现只剩下一个桃子了。求第一天共摘了多少？
#2018-8-5
#---------------------------------------
'''
考虑逆逆向思维问题
'''
'''
t = 1
for i in range(0,10):
    t =1.5+t
print(t)
'''
x2 = 1
for day in range(9,0,-1):
    x1 = (x2+1)*2
    x2 = x1
print(x1)