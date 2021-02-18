#
# 接口测试
# 第三方库：直接拿来用===requests===python实现接口测试
# 一、第三方库安装：
# 1.pip安装
# requests模块安装：pip install requests===user
# 切换源：pip install requests-i http://pypi.tuna.tsinghua.edu.cn/simple/==user
# 加长超时时间：pip-default-timeout 100 install requests
# 注意：修改pip源 可以加快下载安装速度！！
# pip默认使用的pypi的数据源，因为在国外，网速受限，可以修改为国内镜像源，速度快很多。
# a、在系统用户目录下，新建pip文件夹，如：C:\Users\Administrator\pip
# b、再新增 pip.ini文件，粘贴并保存如下内容：
# [global]
# index-url = https://pypi.tuna.tsinghua.edu.cn/simple
# [install]
# trusted-host = https://pypi.tuna.tsinghua.edu.cn
# c、此时pip源已经永久修改生效 ，再执行pip 命令就会快很多，不会报错timeout了！
#
# 2.pycharm安装
# file===setting===project====project interpreter点击+搜索对应的库名字，然后install package即可
# 二、导入： import
# requests 方法的参数传入，除了URL之外，其他的都必须用字典格式传入
#pprint
#注册
import requests,pprint
import jsonpath
url_api_register="http://8.129.91.152:8766/futureloan/member/register"
api_data_register={
  "mobile_phone": "13298568854",
  "pwd": "lemon123456",
  "type":"0",
  "reg_name":"管理员用户lemon"
}
head_register={"X-Lemonban-Media-Type":"lemonban.v2"}
response=requests.post(url=url_api_register,json=api_data_register,headers=head_register)
print(response.json())

#登录

url_api_login="http://8.129.91.152:8766/futureloan/member/login"
api_data_login={
  "mobile_phone": "13298568854",
  "pwd": "lemon123456"
}
head_login={"X-Lemonban-Media-Type":"lemonban.v2"}
response=requests.post(url=url_api_login,json=api_data_login,headers=head_login)
pprint.pprint(response.json())
ret=response.json()
'''
{'code': 0,
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved',
 'data': {'id': 10202298,
          'leave_amount': 0.0,
          'mobile_phone': '13298568854',
          'reg_name': '管理员用户lemon',
          'reg_time': '2021-01-22 09:51:20.0',
          'token_info': {'expires_in': '2021-01-22 10:18:19',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMjAyMjk4LCJleHAiOjE2MTEyODE4OTl9.DHmmx5YMlkWzTmk-uiJ969Yz89Rqlr-HWelT0Nzti9pI07p3FVtwk0kvnsYDybLA0pGPNAr9uvr8RqNpolFH1Q',
                         'token_type': 'Bearer'},
          'type': 0},
 'msg': 'OK'}
'''
#充值
#merber_id=ret["data"]["id"]#取id
#print(merber_id)
#token=ret["data"]["token_info"]["token"]#取token
#print(token)
#安装第三方库，导入,结果放在列表里
#merber_id=jsonpath.jsonpath(ret,"$.data.id")[0]
merber_id=jsonpath.jsonpath(ret,"$..id")[0]#..表示匹配任意次
print(merber_id)
#token=jsonpath.jsonpath(ret,"$.data.token_info.token")[0]
token=jsonpath.jsonpath(ret,"$..token")[0]
url_api_recharge="http://8.129.91.152:8766/futureloan/member/recharge"
api_data_recharge={
  "member_id": merber_id,
  "amount": 0.01
}
head_recharge={"X-Lemonban-Media-Type":"lemonban.v2","Authorization":"Bearer "+token}
response=requests.post(url=url_api_recharge,json=api_data_recharge,headers=head_recharge)
pprint.pprint(response.json())


#访问百度请求
# 1.乱码 ===手动解码
# 2.不是正确的页面===爬虫===反爬机制，检测到你的请求不是浏览器发过来的，不会正确响应
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
#https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=柠檬班
url_bd="https://www.baidu.com/s"
head_bd={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
param={"wd":"柠檬班"}
response=requests.get(url=url_bd,headers=head_bd,params=param)
#print(response.text)#自动解码页面===不能解码成功用另外一种方法
print(response.content.decode("utf8"))#手动解码