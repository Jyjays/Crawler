import utils
from utils import driver

csv_dir = 'D:/Tools/workplace/python_work/Crawler/'
utils.Init('https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS',driver,csv_dir)

utils.input_by_xpath('//*[@id="gradetxt"]/dd[2]/div[2]/input','张学工')
utils.click_by_xpath('//*[@id="gradetxt"]/dd[3]/div[2]/div[1]/div[1]/i')
utils.click_by_xpath('//*[@id="gradetxt"]/dd[3]/div[2]/div[1]/div[2]/ul/li[9]') 
utils.input_by_xpath('//*[@id="gradetxt"]/dd[3]/div[2]/input','清华大学')

# 点击检索
utils.click_by_xpath('//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/input')

# 主要主题数据
#utils.click_by_xpath('//*[@id="divGroup"]/dl[1]/dt/i[1]')
item = utils.parse_outer_text('//*[@id="divGroup"]/dl[1]/dd/div')

# 来源类别
#utils.click_by_xpath('//*[@id="divGroup"]/dl[2]/dt/i[1]')
scource = utils.parse_outer_text('//*[@id="divGroup"]/dl[2]/dd/div')

# 学科
utils.click_by_xpath('//*[@id="divGroup"]/dl[3]/dt/i[1]')
subject = utils.parse_outer_text('//*[@id="divGroup"]/dl[3]/dd/div')

# 研究层次
utils.click_by_xpath('//*[@id="divGroup"]/dl[4]/dt/i[1]')
level = utils.parse_outer_text('//*[@id="divGroup"]/dl[4]/dd/div')

# 年度
utils.click_by_xpath('//*[@id="divGroup"]/dl[5]/dt/i[1]')
year = utils.parse_outer_text('//*[@id="divGroup"]/dl[5]/dd/div')

# 文献来源
utils.click_by_xpath('//*[@id="divGroup"]/dl[7]/dt/i[1]')
source = utils.parse_outer_text('//*[@id="divGroup"]/dl[7]/dd/div')

data_list = [item,scource,subject, level, year, source]
category_list = ['主要主题','来源类型','学科', '研究层次', '年份', '文献来源']

res_list = utils.split_by_enter(data_list, category_list)
utils.write_to_csv('grouped_data.csv', res_list)


#utils.scroll_and_click('//*[@id="gradetxt"]/dd[3]/div[2]/div[1]/div[1]/i','//*[@id="gradetxt"]/dd[3]/div[2]/div[1]/div[2]/ul/li[9]')

driver.quit()
# # 初始化WebDriver
# driver = webdriver.Edge()
# url = 'https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS'
# driver.get(url)
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/input')))

# # 输入查询参数
# driver.find_element(By.XPATH,'//*[@id="gradetxt"]/dd[2]/div[2]/input').send_keys('张学工')
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gradetxt-2"]/div/ul/li[1]/div/label/input')))
# driver.find_element(By.XPATH,'//*[@id="gradetxt-2"]/div/ul/li[1]/div/label/input').click()
# # cssci
# #driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div/label[5]/input').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[1]/span')))
# #driver.click()
# #actions = ActionChains(driver)

# #blank_area = driver.find_element(By.TAG_NAME, 'body')

# # 在空白区域点击
# #actions.move_to_element(blank_area).click().perform()
# driver.find_element(By.XPATH,'//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[1]/span').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/input')))
# #点击检索
# driver.find_element(By.XPATH,'//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/input').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gridTable"]/div/div/div/table/tbody/tr[1]/td[2]/a')))

# # 每页显示条数改成50
# # driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/div/i').click()
# # driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/ul/li[3]/a').click()

# # 主要主题数据  
# #driver.find_element(By.XPATH,'//*[@id="divGroup"]/dl[1]/dt[1]/i[1]').click()  # 此处不需要点击事件，页面生成时已经展开。否则会让数据格式发生变化
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[1]/dd[1]/div')))
# item = driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[1]/dd[1]/div')
# item_outer_text = driver.execute_script("return arguments[0].outerText;", item)

# #print(outer_text)

# #来源类别
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[2]/dt/i[1]')))
# #driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[2]/dt/i[1]').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[2]/dd/div')))
# scource = driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[2]/dd/div')
# scource_outer_text = driver.execute_script("return arguments[0].outerText;", scource)

# #学科
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[3]/dt/i[1]')))
# driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[3]/dt/i[1]').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[3]/dd/div')))
# subject = driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[3]/dd/div')

# subject_outer_text = driver.execute_script("return arguments[0].outerText;", subject)

# #研究层次
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[4]/dt/i[1]')))
# driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[4]/dt/i[1]').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[4]/dd/div')))
# level = driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[4]/dd/div')
# level_outer_text = driver.execute_script("return arguments[0].outerText;", level)

# #年度
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[5]/dt/i[1]'))) 
# driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[5]/dt/i[1]').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[5]/dd/div')))
# year = driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[5]/dd/div')
# year_outer_text = driver.execute_script("return arguments[0].outerText;", year)

# #文献来源
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[7]/dt/i[1]')))
# driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[7]/dt/i[1]').click()
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divGroup"]/dl[7]/dd/div')))
# source = driver.find_element(By.XPATH, '//*[@id="divGroup"]/dl[7]/dd/div')
# source_outer_text = driver.execute_script("return arguments[0].outerText;", source)
# #print(source_outer_text)


# data_list = [item_outer_text,scource_outer_text,subject_outer_text, level_outer_text, year_outer_text, source_outer_text]
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

# # 将分组后的数据写入 CSV 文件
# with open('grouped_data.csv', mode='w', newline='', encoding='utf_8_sig') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Category', 'Keyword', 'Count'])  # 写入标题行
#     for row in res_list:
#         writer.writerow(row)  # 写入每一行

# print("Data has been written to 'grouped_data.csv'.")

# # 写入csv文件
# # with open("主题数据.csv", "w", newline="", encoding='utf_8_sig') as csvfile:
# #     writer = csv.writer(csvfile)
# #     writer.writerow(["主要主题", "数量"])
# #     for row in res_list:
# #         writer.writerow(row)

# # 创建空列表以存储所有元素的文本内容
# # column1_texts = []
# # column2_texts = []
# # column3_texts = []
# # column4_texts = []
# # column5_texts = []
# # column6_texts = []

# # # # 循环遍历每一页
# # while True:
# #     # 获取当前页的元素数量  //*[@id="gridTable"]/div/div/div/table/tbody
    
# #     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gridTable"]/div/div/div/table/tbody')))
# #     elements = driver.find_elements(By.XPATH, '//*[@id="gridTable"]/div/div/div/table/tbody')
# #     elements_count = driver.execute_script("return arguments[0].childElementCount;", elements[0])
# #     # 遍历当前页的元素，获取文本内容并存储到列表中
# #     for i in range(1, elements_count + 1):
# #         # 第一列 文章题目      //*[@id="gridTable"]/div/div/div/table/tbody/tr[2]/td[2]
# #         try:
# #             wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[2]')))
# #             element_col1 = driver.find_element(By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[2]')
# #             title_outer_text = driver.execute_script("return arguments[0].outerText;", element_col1)
# #             column1_texts.append(title_outer_text)
# #         except NoSuchElementException:
# #             column1_texts.append("NA")

# #         # 第二列 作者      //*[@id="gridTable"]/div/div/div/table/tbody/tr[2]/td[3]
# #         try:
# #             wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[3]')))   
# #             element_col2 = driver.find_element(By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[3]')
# #             author_outer_text = driver.execute_script("return arguments[0].outerText;", element_col2)
# #             column2_texts.append(author_outer_text)
# #         except NoSuchElementException:
# #             column2_texts.append("NA")

# #         # 第三列 期刊        //*[@id="gridTable"]/div/div/div/table/tbody/tr[1]/td[4]/span/a  //*[@id="gridTable"]/div/div/div/table/tbody/tr[1]/td[4]/p/a
# #         try:
# #             wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[4]')))   
# #             element_col3 = driver.find_element(By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[4]')
# #             col3_outer_text = driver.execute_script("return arguments[0].outerText;", element_col3)
# #             column3_texts.append(col3_outer_text)
# #         except NoSuchElementException:
# #             column3_texts.append("NA")

# #         # 第四列 时间           //*[@id="gridTable"]/div/div/div/table/tbody/tr[1]/td[5]
# #         try:
# #             wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[5]')))
# #             element_col4 = driver.find_element(By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[5]')
# #             column4_texts.append(element_col4.text)
# #         except NoSuchElementException:
# #             column4_texts.append("NA")
                            
# #         # 第五列 被引       //*[@id="gridTable"]/div/div/div/table/tbody/tr[1]/td[7]/span
# #         try:
# #             wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[7]')))
# #             element_col5 = driver.find_element(By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[7]')
# #             quote_outer_text = driver.execute_script("return arguments[0].outerText;", element_col5)
# #             if quote_outer_text == '':
# #                 column5_texts.append("NA")
# #             else:
# #                 column5_texts.append(element_col5.text)  
# #         except NoSuchElementException:
# #             column5_texts.append("NA")

# #         # 第六列 下载       //*[@id="gridTable"]/div/div/div/table/tbody/tr[1]/td[8]/div/a
# #         try:
# #             wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[8]')))
# #             element_col6 = driver.find_element(By.XPATH, f'//*[@id="gridTable"]/div/div/div/table/tbody/tr[{i}]/td[8]')
# #             download_outer_text = driver.execute_script("return arguments[0].outerText;", element_col6)
# #             if download_outer_text == '':
# #                 column6_texts.append("NA")
# #             else:
# #                 column6_texts.append(element_col6.text)
# #         except NoSuchElementException:
# #             column6_texts.append("NA")


# #     try:
# #         driver.find_element(By.ID, 'PageNext').click()
# #         time.sleep(1)
# #     except NoSuchElementException:
# #         break  # 如果找不到下一页按钮，跳出循环

# # # 写入CSV文件
# # with open("基本信息.csv", "w", newline="", encoding='utf_8_sig') as csvfile:
# #     writer = csv.writer(csvfile)  
# #     for row in zip(column1_texts, column2_texts,column3_texts, column4_texts, column5_texts, column6_texts):
# #         writer.writerow(row)

# # 关闭浏览器
# driver.quit()

