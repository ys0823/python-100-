#----------------------------------------
#要求利用递归函数调用的方式，将获取到所输入的5个字符，以相反顺序分别输出来。
#2018-8-8
#----------------------------------------
s = input('请输入一串字符串:\n')
l = len(s)
def output(s, l): #s为字符串,l为索引,s是一个list
    if l ==0:
        return
    print(s[l-1])
    output(s,l-1)
output(s,l)