
"""为了不像个沙雕一样天天填写重复的健康信息，以下程序用来解决沙雕的
的填报，可以挂载在树莓派上使用，只需要每日定时执行就可以

Chrome版本： 80.0.3987.106
请不要一直执行，我故意设置的time.sleep()一次填写至少要6s，避免给服务器过大负载

需要selenium库支持和Chromedriver支持
"""

from selenium import webdriver
import time
username = ""   #引号内添加一卡通号
password = ""   #引号内输入密码


# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# 授权操作
def operationAuth(driver):
    url = "https://xgbxscwx.seu.edu.cn/?#/ncp-daily-report"
    driver.get(url)
    # 找到输入框并输入查询内容
    elem = driver.find_element_by_id("username")
    elem.send_keys(username)
    # 提交表单
    elem = driver.find_element_by_id("password")
    elem.send_keys(password)
    driver.find_element_by_xpath("//*[@class='auth_login_btn primary full_width']").click()

    time.sleep(3)
    url = "https://xgbxscwx.seu.edu.cn/?#/ncp-daily-report"
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@class='el-button button el-button--primary el-button--large']").click()
    print('今日信息填写完毕')

# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    driver = openChrome()
    operationAuth(driver)