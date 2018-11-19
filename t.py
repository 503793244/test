# from selenium import webdriver
# import time
# # 下载浏览器驱动并根据版本查看对照表
# # 下载谷歌驱动
# # 实例一个浏览器对象：  参数为驱动程序路径
# browser = webdriver.Chrome(executable_path = r'D:\笔记（老师）\爬虫1\4.selenium&phantomjs\谷歌驱动程序\chromedriver.exe') # 注意路径前面加'r'转义
# # 用浏览器对象发送请求：如打开百度
# url = 'http://www.baidu.com'
# browser.get(url)
# time.sleep(5)
#
# # 定位到输入框标签
# input_tag = browser.find_element_by_id('kw')  # 'kw':id名
# # 输入搜索条件：
# input_tag.send_keys('美女')
# # 点击搜索按钮搜索：
# # 先定位：
# input_tag = browser.find_element_by_id('kw')
# # 点击：
# input_tag.click('su')
# time.sleep(5)
#
# browser.quit()

from selenium import webdriver
import time

browser = webdriver.PhantomJS(executable_path = r'D:\笔记（老师）\爬虫1\4.selenium&phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe') # 注意路径前面加'r'转义

# 用浏览器对象发送请求：(豆瓣电影)
url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='
browser.get(url)
# 给一点时间执行操作：
time.sleep(2)

# 使浏览器滚动条拖到可视窗口最下JS代码：
js = 'window.scrollTo(0,document.body.scrollHeight)'  # 0:横坐标  document.body.scrollHeight：窗口长

# 执行JS代码：
browser.execute_script(js)  # 执行一次拖动一次
time.sleep(2)

browser.execute_script(js)  # 执行一次拖动一次
time.sleep(2)

# 获取页面数据(不需要再用requests模块，直接从browser对象中的'page_source'属性中获取)：
page_text = browser.page_source

# 解析数据

# 持久化
# with open('./page_1.html','w',encoding='utf-8') as f:
#     f.write(page_text)

# 也可截图查看
print(333)
print('junjie001branch')
browser.save_screenshot('./page_1.png')
