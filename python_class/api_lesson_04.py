'''
一、函数：有一段代码，重复使用到，把这段代码进行一个封装===函数===调用这个函数
作用：提高代码的复用率
格式：
def 函数名():
函数体（真正实现具体功能的代码）
注意：函数依然是一个标识符，命名规则6点
      函数定义完之后，没有被调用不会执行
      要写函数名调用
      函数里面可能会变化的内容，不建议写在函数里面====参数化
      定义参数类型
      1、必备参数：定义了就必须要传入参数，不传或者少传了都会报错的
      2、默认参数：如果有些参数有一些大概率的情况===值===用默认值===可以不传===也可以传入（替换默认值）
      3、不定长参数：不确定是否有，也不确定有多少的这种参数
      *args 等到前面的必备参数和默认参数都接受完成之后，剩下的参数都会被这个不定长参数接受，并且以元组的格式保存
      ---多余参数用的位置传参的方式，被*不定长参数接受
      注意：位置不一定在最后
      **kwargs 等到前面的必备参数和默认参数都接受完成之后，剩下的参数都会被这个不定长参数接受，并且以字典的格式保存
      ---多余参数用的关键字传参的方式，被**不定长参数接受
      注意：位置一定在最后
      参数传入的方式：
      1.位置传参方式：位置的顺序性===传错了位置，参数错了===简单容易出错
      注意：必备参数必须要放在默认参数的前面
      2、关键字传承参：指定参数名进行传参===精确点，不容易出错
      3.混合传参：位置传参必须放在关键字传参前面
二、断点调试
1、方便理解原理执行过程
2、寻找问题==调试
'''
'''
print("aa")
def good_job(salary,bonus,subsidy=200,*args,**kwargs): #定义函数====定义参数（形参）
    print("参数salary: {}".format(salary))
    print("参数bonus: {}".format(bonus))
    print("参数subsidy: {}".format(subsidy))
    print("参数*args: {}".format(args))
    print("参数*kwargs: {}".format(kwargs))
    sum1=salary+bonus+subsidy
    for i in args:
        sum1+=i
    for j in kwargs:
        print(kwargs[j])
        sum1+=kwargs.get(j)
    print("工资总和：{}".format(sum1))
#good_job(7000,1000,100,100,20)#调用函数===传参（实参）
#good_job(7000,bonus=1000,subsidy=100,111,222,aa=100,bb=100)#调用函数===传参（实参）
#good_job(7000,1000,100,1,2,aa=100,bb=100)#调用函数===传参（实参）
'''

'''
返回值：函数如果有一个数据需要给到调用这个函数的人去使用的话，把这个数据的变量设置为函数的返回值
1.返回值一定是最后，返回值后面的代码不会再执行===标志函数的结束】
2.返回值是可以没有的==None:有一个，可以有多个====返回值之间用逗号隔开，用元组来接受的
'''
print("qq")
def good_job(salary,bonus,subsidy=200,*args,**kwargs): #定义函数====定义参数（形参）

    sum1=salary+bonus+subsidy
    for i in args:
        sum1+=i
    for j in kwargs:
        sum1+=kwargs.get(j)
    return  sum1,salary #定义函数返回值
#函数定义返回值之后，用变量接受函数的调用的时候===函数的返回值
result=good_job(7000,1000,100,1,2,aa=100,bb=100)#调用函数===传参（实参）
print(result)


'''
内置函数
print()
input()
type()
isinstance()
len()
数据类型str(),int(),float(),list(),tuple(),dict(),set(),bool()
字符串的内置方法：  .format，index ,replace,find,count....
列表内置方法：appand,insert ,pop ,remove,extend,count
字典内置方法：pop, update ,get ...
range():
'''


#作业练习
#1.
str2='hello'
list1=list(str2)
print(list1)
#2.
'''
num1=int(input("请输入数字："))
sum2=0
for num in range(num1):
    sum2+=num
    print(sum2)
'''
#3
print("aa")

def istrue(sb):
    print("bb")

    if type(sb)==list or type(sb)==dict or type(sb)==str:
        length=len(sb)
        if length>=5:
            print("true")
        else:
            print("false")
    else:
        print("数据类型不能计算长度")
        print("bb")
istrue([1, 2, 3, 4,5])



