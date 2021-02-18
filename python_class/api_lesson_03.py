'''
一、列表：list []
1.列表可以存放任意数据类型，包括列表，元素和元素之间用英文逗号隔开
2.列表统计元素个数：len()
3.取值：每个元素都有自己的位置===索引从0开始
  取多个值：切片
4.列表的元素可以被改变的：增加、删除、修改
5.列表的元素是可以重复的，重复的次数===count()
'''
list1 =[20,"may",True,[1,2,3]]
print(len(list1))
print(list1[1])
print(list1[0:3:1])
print(list1[-1][2])#扩展列表的嵌套取值
#增加
list1.append("cheng")#追加元素到末尾===p1
print(list1)
list1.insert(3,'ying')#指定位置进行元素的增加===p1
print(list1)
list1.extend(["aa","bb"])#合并，可以同时添加多个元素===扩展
print(list1)
#删除
list1.pop()#默认删除最后一个元素
print(list1)
list1.pop(5)#可以指定元素索引进行删除
print(list1)
list1.remove("may")#指定元素本身进行删除
print(list1)
#list1.clear()#清空
#修改
list1[0]="aa"
print(list1)
list1.count("aa")
print(list1.count("aa"))

'''
元组：tuple()

1.元组可以存放任意数据类型，元组和元组之间用英文逗号隔开
2.元组统计元素个数：len()
3.取值：每个元组都有自己的位置===索引从0开始
  取多个值：切片
4.元组的元素不可以被改变的
5.列表的元素是可以重复的，重复的次数===count()
扩展：想要改变元组的元素=====列表===list()----元组==tuple()
'''
tuple1=('aa', True, 'ying', [1, 2, 3], 'aa')
print(tuple1)
list2=list(tuple1)
print(list2)
list2[0]="cc"
print(list2)
tuple2=tuple(list2)
print(tuple2)

'''
字典：dict {}
1.元素是键值对的格式：key:value====一个键值对是一个元素，多个元素之间用逗号隔开
2.字典一般的使用场景：描述一个物件的属性：名字、年龄、性别
3.取值：通过key来取value值
4.key:（1）不可变的（不可以是列表、字典）（2）key不可以重复； value：没有任何要求===可以被改变--增加、修改、删除
5.统计元素个数===len()
注意：字典在3.6版本之前没有顺序的，没有索引
'''
dict1={"name":"abc","age":"18","gender":"male"}
#print(dict1["age"])
#print(dict1.get("age"))
#增加/修改===加一个键值对
dict1["hobby"]="吃"#如果key不存在新增加一个键值对元素
print(dict1)
dict1["gender"]="female"#如果key存在更新一个键值对value
print(dict1)
#增加多个===update 字典合并操作
dict1.update({"city":"长沙","hight":"100"})
#删除==指定key进行删除
#dict1.pop("hobby")
print(dict1)
#统计
print(len(dict1))

'''
集合 set{} 元素单个====扩展
1.集合的元素不重复的，===使用场景就是给列表去重
2.无顺序的
'''
#set1={1,1,2,2,3,4}
#print(set1)
list3=[1,1,2,2,3]
print(list3)
set2=set(list3)#转化为集合 去重
print(set2)

'''
控制流：if判断  for循环===分支
if判断语法：
if 条件:===判断这个条件成立的时候，进入下面执行语句--分支==看见：有四个空格的缩进
    子代码（执行语句）
elif 条件:===判断这个条件成立的时候，进入下面执行语句--分支
    子代码（执行语句）
elif 条件:===注意：elif可以没有，可以多个
    子代码（执行语句）
else===没有条件的
  子代码（执行语句） 
'''

#money=int(input("请输入金额："))
#if money>=100:
#    print("买house")
#elif money>=20:
#    print("买che")
#else:
#    print("好好赚钱")

'''
for 循环：重复执行某一块代码
使用场景：用来遍历某些数据对象的元素====字符串、列表、元组、字典
缩进里面是for循环的循环体
循环次数由元素个数决定
控制循环体：====if判断，break，continue
for 循环结合使用的一个内置函数：range()===生成一个整数序列
start:从谁开始生成，默认值0
stop:到谁结束===不能省略
step:步长===默认值为1
'''
count=0
str1="hello python"
for i in str1:
    print(i)
    print("*"*20)
    count +=1
    print(len(str1))
    print(count)

list4=[20,"may",True,[1,2,3]]
for j in list4:
    if j=="may":
        break
     #break #中断====跳出了整个循环
    #continue #继续====跳出本次循环
    print(j)


for num in range(0,11,2):
    print(num)

#总结：内置函数：input() print()

#课后作业
#1
a=[1,2,'6','summer']
if "i" not in a:
   print("i不在这个列表里面")
#2
dict_1={"class_id":45,'num':20}
if dict_1["num"]>=5:
    print("这个班级的人数是：{}".format( dict_1["num"]))
else:
    print("这个班级的人数不足5人")

'''
list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
list5=[{"name":"肥兔","age":"18","gender":"male"},
       {"name":"鹿鹿","age":"18","gender":"male"},
       {"name":"Freestyle","age":"18","gender":"male"},
       {"name": "等", "age": "18", "gender": "male"},
       {"name": "地球", "age": "18", "gender": "male"},
       {"name": "阑珊", "age": "18", "gender": "male"},
       {"name": "柠檬", "age": "18", "gender": "male"}
       ]
print(list5)
'''
'''
list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
list2=[]
for i in list1:
    dict1=dict(name=i,age=18,gender="男")
    list2.append(dict1)
print(list2)
'''

#4 循环字典、元组
dict1 = {"name": "abc", "age": "18", "gender": "male"}
for k in dict1:
   print(k)

tuple1=('aa', True, 'ying', [1, 2, 3], 'aa')
for j in tuple1:
    print(j)








