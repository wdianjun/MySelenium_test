# 1.导包
from selenium import webdriver
import time
# 2.创建浏览器驱动对象
driver = webdriver.Chrome()

# 3.打开测试网址
driver.get("file:///D:/test/%E9%BB%91%E9%A9%AC24%E8%B5%84%E6%96%99/UI%E8%87%AA%E5%8A%A8%E5%8C%96/web%E7%8E%AF%E5%A2%83/%E6%B3%A8%E5%86%8CA.html")

# 4.暂停3秒 代替测试步骤
time.sleep(3)

# 使用id定位 输入用户名：admin
driver.find_element("id", "userA").send_keys("admin")
# 使用id定位 输入密码：passwordgit
driver.find_element("id", "passwordA").send_keys("password")

time.sleep(3)
# 5.关闭浏览器
driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# # 快速配置
# options = Options()
# options.page_load_strategy = 'eager'

# driver = webdriver.Chrome(options=options)

# start_time = time.time()
# driver.get("http://www.baidu.com")
# load_time = time.time() - start_time
# print(f"页面加载耗时: {load_time:.2f}秒")

# time.sleep(3)

# driver.quit()
# print("浏览器已关闭")