import utils
from selenium.common.exceptions import NoSuchElementException

# 初始化WebDriver
from utils import driver

paper_list = '/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div'

year_path = '/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[1]/i'
year_list = '/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div'



# 以下是万方网站特定函数
def WANFANG_set_class1_author():
    # utils.click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/i')
    # utils.click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul[2]/li[5]')
    utils.scroll_and_click('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/i','/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul[2]/li[5]')
def WANFANG_input_second_part(author):
    utils.input_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/input',author)
def WANFNAG_set_class2_authorhome():
    # utils.click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div/i')
    # utils.click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/ul[2]/li[6]')
    utils.scroll_and_click('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div/i','/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/ul[2]/li[6]')
def WANFANG_input_third_part(home):
    utils.input_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/input',home)
#不限：/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[1]/div[2]/ul[2]/li[1]
#19年：/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[1]/div[2]/ul[2]/li[7]
#不限用0代替
def WANFANG_set_time_range(time1,time2):
    #设置起始时间
    if time1 == 0:
        to_click = 1
    else:
        to_click = 2024 - time1 + 2
    utils.scroll_and_click('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[1]/div[1]/div/i','/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[1]/div[2]/ul[2]/li['+str(to_click)+']')
    #设置终止时间
    #utils.click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[2]/div[1]/div/i')
    #网站原因，要点击两次
    #click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[2]/div[1]/div/i')
    if time2 == 0:
        to_click = 1
    else:
        to_click = 2024 - time2 + 2
    #click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[2]/div[2]/ul[2]/li['+str(to_click)+']')
    utils.scroll_and_click('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[2]/div[1]/div/i','/html/body/div[5]/div/div[2]/div[2]/div[1]/div[3]/span[1]/span[2]/div[2]/div[2]/ul[2]/li['+str(to_click)+']')
#  点击搜索
def WANFANG_click_search():
    utils.click_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[1]/div[4]/span[1]')
utils.Init('https://s.wanfangdata.com.cn/advanced-search/paper',driver)



WANFANG_set_class1_author()
WANFANG_input_second_part('张学工')
WANFNAG_set_class2_authorhome()
WANFANG_input_third_part('清华大学')
WANFANG_set_time_range(2014,0)
#点击搜索
WANFANG_click_search()
#/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div

# 根据年份获取文献数量
utils.click_by_xpath(year_path)
year_outer_text = utils.parse_outer_text(year_list)


# 获取当前页的文章数量
category_data = [['期刊论文',0],['会议论文',0]]
item_data = []
num = utils.parse_element_count(paper_list)

while True:
    for i in range(1,num):
        category = utils.parse_outer_text(f'/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div[2]/span[1]')
        if category == '[期刊论文]':
            category_data[0][1] += 1
        elif category == '[会议论文]':
            category_data[1][1] += 1
        item_count = utils.parse_element_count(f'/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div[4]')
        if item_count == 0 | item_count == ():
            continue
        for j in range(1,item_count+1):
            item = utils.parse_outer_text(f'/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div[4]/span[{j}]')
            item_data.append(item)

    item_map = []
    for item in item_data:
        if item in item_map:
            item_map[item_map.index(item)][1] += 1
        else:
            item_map.append((item,1))
    # 如果有下一页则点击下一页
    try:
        # 自行填入下一页的xpath
        # utils.click_by_xpath_no_wait('')
        # 因为本次爬取没有下一页，所以直接break
        break
    except NoSuchElementException:
        break

print(category_data)
# 关闭浏览器
driver.quit()

