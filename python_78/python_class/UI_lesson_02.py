'''
web页面基本组成：html+css+js(javascript)
html:定义页面呈现内容：标签语言
css:控制页面如何呈现：布局、字体颜色
js:可以让页面在不同情况下，做不同的事情

HTML页面：标签===属性
页面元素定位：能够唯一标识这个元素的内容（按照开发遵循原则的基础上===元素属性里面 ID name 唯一）
一、元素定位八大方法:id,name,xpath,css,class,tag,link,partial_link
（1）通过Id name 可以找到这个元素，大部分的元素没有这两个属性，xpath
（2）xpath元素定位方法：
绝对路径复制xpatch:/html/body/div/div/div[1]/a/small====从根开始，一级一级往下找==继承、顺序，
所以页面一旦发生变化，修改代码===不好用，用的少
相对路径： //small     //*[@id="username"]===以双//开头的，不考虑兄弟、祖先、父亲，靠自己
如果万一不行，偶尔靠亲戚====更多
xpath元素定位
1.相对路径:标签名+属性
绝对路径：//标签名[@属性名=属性值]=====属性比较有标识性
//input[@id="username"]
2.层级定位
//标签名[@属性名=属性值]
//div[@class="login-logo"]//b
3.文本属性定位===当值不变的，唯一标识
//b[text()="柠檬ERP"]  ; //b[text()="[ 立即注册 ]"]
4.包含属性值：//标签名[contains(@属性名/text(),属性值)]====值/属性内容太长
//input[contains(@name,"username")]  ； //b[contains(text(),"柠檬")]
5.轴定位
//input[@id="rememberUserCode"]/following-sibling::ins ==跟随后面 ； preceding-sibling

二、找到元素后的四大操作
点击：click
输入内容：send_keys
获取文本：text
获取属性：attribute


三、python 三大等待===python 等待：一般当你打开新页面（click操作之后）页面刷新时间===等待
1.强制等待===sleep()设置等待时长没有到期就算元素出现了，也还要等待===速度慢
2.智能等待：
        （1）隐性等待：默认等待时间，只要元素出现了，直接继续往下执行====一个会话只执行一次
            默认等待设置的时长，提前出现，提前执行，有些地方不生效+强制等待
        （2）显示等待===复杂==了解




'''


from selenium import webdriver #从selenium这个工具导入webdriver库
import time
driver=webdriver.Chrome() #初始化一个浏览器=====会话session
driver.implicitly_wait(10)#隐性等待
driver.get("http://erp.lemfix.com/")#打开浏览器对应的网址
driver.maximize_window()
title=driver.title#获取页面的标题
if title=="柠檬ERP":
    print("页面标题是：{}".format(title))
else:
    print("这个用列不通过")
#输入用户名，密码进行登录操作
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins ").click()
driver.find_element_by_id("btnSubmit").click()
time.sleep(2)
#确认登录用户名
page_name=driver.find_element_by_xpath("//p").text #获取元素的文本内容
if page_name=="测试用户":
    print("登陆的的用户是：{}".format(page_name))
else:
    print("这个用列不通过")
