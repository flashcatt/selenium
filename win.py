from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化 WebDriver（以 Edge 为例）
driver = webdriver.Edge(executable_path="c:/Users/23202/Desktop/test1/py/msedgedriver.exe")

# 基础 URL
base_url = "https://detail.zol.com.cn/cell_phone_index/subcate57_544_list_1_0_1_1_0_"

# 总页数，可以根据实际情况调整
total_pages = 5
i=0
for page in range(1, total_pages + 1):
    url = base_url + str(page) + ".html"
    driver.get(url)
    print(f"访问页面: {url}")
    time.sleep(1)  # 等待页面加载完成
    # 获取所有窗口句柄
    allhandles = driver.window_handles
    print("目前有", allhandles)
    print("当前句柄", driver.current_window_handle)
    
    print("初始界面")
    # 获取所有手机页面元素
    print("正在获取所有手机页面元素")
    div_elements = driver.find_elements(By.CSS_SELECTOR, "div.list-item.clearfix h3 a")
    
    for element in div_elements:
        # 点击进入手机页面
        element.click()
        print("进入手机页面界面")
        time.sleep(1)
        
        # 获取所有窗口句柄并切换到手机页面句柄
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[1])
        print("当前是", driver.current_window_handle)
        
        print(driver.title)  # 获取页面标题
        time.sleep(0.5)  # 等待
        
        # 点击参数，进入参数页面
        element1 = driver.find_element(By.PARTIAL_LINK_TEXT, "参数")  # 定位元素
        element1.click()  # 点击参数
        time.sleep(1)
        allhandles = driver.window_handles  # 获取所有窗口句柄
        print("进入点击参数界面")
        print("目前有", allhandles)
        print("当前是", driver.current_window_handle)
        time.sleep(0.5)  # 等待
        driver.switch_to.window(allhandles[1])  # 切换到新页面句柄
        
        element2 = driver.find_element(By.XPATH, "//span[contains(text(), '复制图文混排表格')]")
        element2.click()  # 点击复制，跳出小框
        time.sleep(1)
        allhandles = driver.window_handles  # 获取所有窗口句柄
        print("已点击复制图文混排表格")
        print("目前有", allhandles)
        print("当前是", driver.current_window_handle)
        
        # 切换到 iframe
        iframe = driver.find_element(By.ID, 'ifraMixed')  # 定位 iframe
        driver.switch_to.frame(iframe)  # 切换到 iframe
        
        # 点击预览
        element3 = driver.find_element(By.ID, "viewPage")  # 定位元素
        element3.click()  # 点击预览，进入表格页面
        print("已点击预览")
        print("进入表格页面界面")
        time.sleep(0.5)  # 等待
        allhandles = driver.window_handles  # 获取所有窗口句柄
        driver.switch_to.window(allhandles[2])  # 切换到表格页面句柄
        print("目前有", allhandles)
        print("当前是", driver.current_window_handle)
        page_source = driver.page_source  # 获取页面源代码
        
       
        
        page_source = driver.page_source
        
        i += 1
        print("正在打印第", i)
        file_path = f"C:/Users/23202/Desktop/test1/py/data/response_data_{i}.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(page_source)
        driver.close()
        
        print("已关闭表格页面")
        allhandles = driver.window_handles  # 获取所有窗口句柄
        driver.switch_to.window(allhandles[1])
        print("目前有", allhandles)
        print("当前是", driver.current_window_handle)
        driver.close()
        print("已关闭参数页面")
        allhandles = driver.window_handles  # 获取所有窗口句柄
        print("目前有", allhandles)
        driver.switch_to.window(allhandles[0])
        print("当前是", driver.current_window_handle)
        
        print("已切换到主页面")
        print("正在打印数据")

# 关闭浏览器
driver.quit()