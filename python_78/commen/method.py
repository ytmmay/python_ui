import  time
#打开浏览器函数
def openurl(driver,url):
    driver.get(url)  # 打开浏览器对应的网址
    # 浏览器最大化
    driver.maximize_window()

#登录函数
def login(driver,username,password):
    driver.find_element_by_id("username").send_keys("test123")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins ").click()
    driver.find_element_by_id("btnSubmit").click()


#搜索的函数
def search_fun(driver,url,username,password,key):
    openurl(driver, url)
    login(driver, username, password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()  # 点击零售出库
    # driver.switch_to.frame("tabpanel-7d03ccc88e-frame")#id是变化的不能直接使用
    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")  # 找到元素，获取D属性
    id_frame = id_li + "-frame"  # 得到iframe id
    driver.switch_to.frame(id_frame)  # 通过iframe id 进行iframe切换
    # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))#web element切换子页面
    driver.find_element_by_id("searchNumber").send_keys(key)  # 找到搜索输入框
    driver.find_element_by_id("searchBtn").click()  # 点击查询按钮
    time.sleep(1)  # 隐士等待+强制等待的使用
    number = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text  # 获得单据编码的号码
    return number