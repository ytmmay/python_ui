'''
自动化类型：
接口自动化：===接口最多，稳定，性价比最高的===回归测试
UI自动化：性价比低，维护成本高===冒烟测试
APP自动化

UI自动化：
python代码===翻译（中间件）===浏览器   驱动可以把代码的指令翻译给浏览器，浏览器可以做响应的操作
          浏览器驱动：
          chromedriver
           geckodriver
           ieserverdriver
 谷歌驱动：http://npm.taobao.org/mirrors/chromedriver/
火狐：https://github.com/mozilla/geckodriver/releases
ie:http://selenium-release.storage.googleapis.com/index.html
selenium工具包：UI自动化工具===第三方库
ide:===录制脚本===少，不好用
webdriver:库=====提供了对网页各种操作方法，提供了各种语言版本====python java ===结合语言来用
grid:分布式====同时对多个浏览器执行并发的

1.selenium安装好
2.驱动下载===python 对应的安装目录
3.导入selenium webdriver
通讯原理：
1、chromedriver启动服务，ip端口监听
2、python webdriver 跟 chromedriver 建立连接，发送http请求
3、chromedriver 收到指令之后，驱动浏览器把指令执行
4、chromedriver 要返回结果给webdriver
后续指令重复这个步骤

'''
from selenium import webdriver #从selenium这个工具导入webdriver库
import time
driver=webdriver.Chrome() #初始化一个浏览器=====会话session
driver.get("https://www.baidu.com")#打开浏览器对应的网址
#浏览器最大化
driver.maximize_window()
#返回上一页面，前进一个页面，刷新
#driver.get("https://www.taobao.com/")


time.sleep(2)
driver.back()
driver.forward()
driver.refresh()
#关掉浏览器 close():关闭窗口，不会退出浏览器；quit()===退出当前会话，关闭浏览器，清除缓存
driver.close()



