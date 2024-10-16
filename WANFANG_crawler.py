import utils

# 初始化WebDriver
from utils import driver


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
# 获取当前页的文章数量
num = utils.parse_element_count('/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div')
for i in range(1,num+1):
    category = utils.parse_outer_text(f'/html/body/div[5]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div[2]/span[1]')
    if category == '[期刊论文]':
        print('期刊论文')
    elif category == '[会议论文]':
        print('会议论文')
        

# 关闭浏览器
driver.quit()

