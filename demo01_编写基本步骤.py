# 1.导包
from selenium import webdriver
import time
# 2.创建浏览器驱动对象
driver = webdriver.Chrome()

# 3.打开测试网址
driver.get("https://chat.deepseek.com/")

# 4.暂停3秒 代替测试步骤
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