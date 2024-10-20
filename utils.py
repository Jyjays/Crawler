from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv
import os


# 初始化WebDriver
driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)
# 初始化要爬取的网址
def Init(URL,driver,dir):
    driver.get(URL)
    os.chdir(dir)
    #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/input')))

# 等待元素加载
def wait_by_xpath(xpath):
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

# 点击事件
def click_by_xpath(xpath):
    wait_by_xpath(xpath)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    #wait.until_not(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).click()

# 不需要等待的点击事件
def click_by_xpath_no_wait(xpath):
    driver.find_element(By.XPATH, xpath).click()

# 滑动事件
def scroll_down(xpath_to_option):
    while True:
        try:
            # 尝试找到目标选项
            option = driver.find_element(By.XPATH, xpath_to_option)
            # 滚动到该选项
            driver.execute_script("arguments[0].scrollIntoView(true);", option)
            return option
        except:
            # 找不到则继续滚动页面
            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()
# 滑动点击函数
def scroll_and_click(dropdown_xpath, option_xpath):
    # 打开下拉菜单
    click_by_xpath(dropdown_xpath)
    
    # 滑动到目标选项并点击
    option = scroll_down(option_xpath)
    option.click()

# 输入事件
def input_by_xpath(xpath, text):
    wait_by_xpath(xpath)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).send_keys(text)

# 解析元素文本
def parse_outer_text(xpath):
    wait_by_xpath(xpath)
    element = driver.find_element(By.XPATH, xpath)
    return driver.execute_script("return arguments[0].outerText;", element)
# 解析元素数量
def parse_element_count(xpath):
    wait_by_xpath(xpath)
    element = driver.find_element(By.XPATH, xpath)
    return driver.execute_script("return arguments[0].childElementCount;", element)

# 按空格分割数据
def split_by_space(data):
    return data.split('\n')

# 按'\n'分割数据
def split_by_enter(data,category_list):
    res_list = []
    for index, data in enumerate(data):
        category = category_list[index]  # 对应的类别标签
        for line in data.split('\n'):
            if '(' in line and ')' in line:
                keyword = line[:line.rfind('(')].strip()
                value = int(line[line.rfind('(')+1:line.rfind(')')])
                res_list.append((category, keyword, value))
    return res_list
    

#data_list = [item_outer_text,scource_outer_text,subject_outer_text, level_outer_text, year_outer_text, source_outer_text]
# category_list = ['主要主题','来源类型','学科', '研究层次', '年份', '文献来源']  
# res_list = []

# # for index, data in enumerate(data_split_by_space):
# #     category = category_split_by_space[index]  
# #     for line in data.split(' '):
# #         if '(' in line and ')' in line:
# #             keyword = line[:line.rfind('(')].strip()
# #             value = int(line[line.rfind('(')+1:line.rfind(')')])
# #             res_list.append((category, keyword, value))


# for index, data in enumerate(data_list):
#     category = category_list[index]  # 对应的类别标签
#     for line in data.split('\n'):
#         if '(' in line and ')' in line:
#             keyword = line[:line.rfind('(')].strip()
#             value = int(line[line.rfind('(')+1:line.rfind(')')])
#             res_list.append((category, keyword, value))
# 写入csv文件
def write_to_csv(file_name, res_list):
    with open(file_name, "w", newline="", encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        # 写入标题行
        writer.writerow(['Category', 'Keyword', 'Count'])
        #writer.writerow(category_list)
        for row in res_list:
            writer.writerow(row)
# with open('grouped_data.csv', mode='w', newline='', encoding='utf_8_sig') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Category', 'Keyword', 'Count'])  # 写入标题行
#     for row in res_list:
#         writer.writerow(row)  # 写入每一行
