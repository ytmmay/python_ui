lemon="1"
print(lemon)
print("aa" + lemon+"")

print(''' 
name:{}'''.format(lemon))

print(''' 
name:%s'''%(lemon))
#1.取值：每个元素都有位置====索引从0开始 str[]
#取最后一个元素：-1
#2.取多个值：切片===指定[索引头：索引尾：步长]===取头不取尾
#头默认值从0开始
#索引尾默认值：最后
#步长：1
str1="hello"
print(str1[-1])
print(str1[0:4:1])

#3.获取长度：len()
print(len(str1))
#4.获取某个元素的索引
#print(str.index("q")) #没有找到元素会报错====代码会停止运行
print(str1.find("q")) #没有找到元素不会会报错====代码不会停止运行

#5.统计个数
print(str1.count("o"))
#6.元素的替换===旧的内容替换新的内容
print(str1.replace("hello","hi"))

#1.算术运算符：+ - * /
print(1+1)
#2.数据类型的强制转换：str()   int() float()
print('aa'+ str(100))
#3.input()===获取从控制台进行输入的内容===输入的任何内容都是字符串
#num1=input("请输入一个数字：")
#print(int(num1)+1)
#2.赋值运算符 == == 符号右边的内容赋值给左边的内容 =， += ， -=
a=10
a+=5#a=a+5
print(a)
#3.比较运算符 > < == >= <= !=   ==可以判断字符串是否相等==用于断言    =====运行结果是bool值
print(4>3)
print("aa"=="aa")

#4.逻辑运算符： and 与 or 或not 非 == == = and 真真为真， or 假假为假
print(4>5 and 5<7)
print(4>5 or 5<7)
# 5.成员运算符: in  not in
str2="hello word"
print("h" in str2)

#第二节课作业
#1
#name=input("请输入姓名：")
#age=input("请输入年龄：")
#sex=input("请输入性别：")
#print('''*********************''')
#print("姓名:"+name)
#print("姓名:"+age)
#print("姓名:"+sex)
#print('''*********************''')
#name=input("请输入姓名：")
#age=input("请输入年龄：")
#sex=input("请输入性别：")
#print('''*********************
#姓名:{}
#年龄:{}
#性别:{}
#'*********************'''.format(name,age,sex))


#2
str2='python hello aaa 123123aabb'
print(str2[0:6:1])

#print(str2.find("o a"))
#print(str2.find("he"))
#print(str2.find("ab"))

print("o a" in str2)
print("he" in str2)
print("ab" in str2)


print(str2.replace("python","lemon"))
print(str2.find("aaa"))
