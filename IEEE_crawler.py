import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def crawl_ieee_xplore(sort):
    driver_path = ChromeDriverManager().install()
    chrome_options = webdriver.ChromeOptions()

    # 禁止加载图片等资源
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-extensions")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service,options=chrome_options)
    
    driver.maximize_window()
    driver.get('https://ieeexplore-ieee-org-s.webvpn.cumt.edu.cn:8118/Xplore/home.jsp')

    WebDriverWait(driver, 120).until(
        ec.presence_of_element_located((By.XPATH,
                                        '//*[@id="LayoutWrapper"]/div/div/div[3]/div/xpl-root/header/xpl-header/div/div[2]/div[2]/xpl-search-bar-migr/div/form/div[2]/div/div[1]/xpl-typeahead-migr/div/input'))
    )

    search_box = driver.find_element(By.XPATH,
                                     '//*[@id="LayoutWrapper"]/div/div/div[3]/div/xpl-root/header/xpl-header/div/div[2]/div[2]/xpl-search-bar-migr/div/form/div[2]/div/div[1]/xpl-typeahead-migr/div/input')
    search_box.send_keys('Blockchain')
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 120).until(
        ec.presence_of_all_elements_located((By.XPATH,
                                             '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-search-results/div/div[2]/div[2]/xpl-results-list/div[2]/xpl-select-dropdown/div/button'))
    )

    if sort == "newest":
        drop_down = driver.find_element(By.XPATH,
                                        '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-search-results/div/div[2]/div[2]/xpl-results-list/div[2]/xpl-select-dropdown/div/button')
        drop_down.click()

        newest = driver.find_element(By.XPATH,
                                     '//*[@id="xplMainContent"]/div[2]/div[2]/xpl-results-list/div[2]/xpl-select-dropdown/div/div/button[2]')
        newest.click()

    articles = []

    for i in range(1, 6):

        print(f'\n********** Page number {i} **********\n')

        for j in range(3, 28):

            print(f'Article number {j - 2}:')

            WebDriverWait(driver, 120).until(
                ec.presence_of_all_elements_located((By.XPATH,
                                                     '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-search-results/div/div[2]/div[2]/xpl-results-list/div[27]/xpl-results-item/div[1]/div[1]/div[2]/h3/a'))
            )

            back_url = driver.current_url

            type_ = driver.find_element(By.XPATH,
                                        f'/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-search-results/div/div[2]/div[2]/xpl-results-list/div[{j}]/xpl-results-item/div[1]/div[1]/div[2]/div/div[1]/span[2]/span[2]').text
            if type_ != "Conference Paper":
                continue

            open_article = driver.find_element(By.XPATH,
                                               f'/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-search-results/div/div[2]/div[2]/xpl-results-list/div[{j}]/xpl-results-item/div[1]/div[1]/div[2]/h3/a')
            open_article.click()

            WebDriverWait(driver, 120).until(
                ec.presence_of_all_elements_located((By.XPATH, '/html'))
            )

            # title_____________________________________________________________________________________________________
            title = ''
            try:
                title = driver.find_element(By.XPATH,
                                            '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/section[2]/div/xpl-document-header/section/div[2]/div/div/div[1]/div/div[1]/h1/span').text
            except:
                title = ''
            print("\ttitle:", title)

            # Page(s)___________________________________________________________________________________________________
            page = 0
            try:
                page = driver.find_element(By.XPATH,
                                           '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[2]/div[1]/div[1]/span').text.strip(
                    '- ')
                page = int(page)
            except:
                page = 0
            print("\tPage(s):", page)

            # Cites in Papers___________________________________________________________________________________________
            papers = 0
            try:
                papers = driver.find_element(By.XPATH,
                                             '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/section[2]/div/xpl-document-header/section/div[2]/div/div/div[3]/div[2]/div[1]/div[1]/button[1]/div[1]').text
                papers = int(papers)
            except:
                papers = 0
            print("\tCites in Papers:", papers)

            # Cites in Patent___________________________________________________________________________________________
            patent = 0
            try:
                patent = driver.find_element(By.XPATH,
                                             '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/section[2]/div/xpl-document-header/section/div[2]/div/div/div[3]/div[2]/div[1]/div[1]/button[2]/div[1]').text
                patent = int(patent)
            except:
                patent = 0
            print("\tCites in Patent:", patent)

            # Full Text Views___________________________________________________________________________________________
            views = 0
            try:
                views = driver.find_element(By.XPATH,
                                            '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/section[2]/div/xpl-document-header/section/div[2]/div/div/div[3]/div[2]/div[1]/div[1]/button[3]/div[1]').text
                views = int(views)
            except:
                views = 0
            print("\tFull Text Views:", views)

            # Publisher_________________________________________________________________________________________________
            publisher = ' '
            try:
                publisher = driver.find_element(By.XPATH,
                                                '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[3]/div[2]/div[2]/xpl-publisher/span/span/span/span[2]').text
            except:
                publisher = ''
            print("\tPublisher:", publisher)

            # DOI_______________________________________________________________________________________________________
            doi = ''
            try:
                doi = driver.find_element(By.XPATH,
                                          '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[3]/div[2]/div[1]/a').text
            except:
                doi = ''
            print("\tDOI:", doi)

            # Date of Publication_______________________________________________________________________________________
            date = ''
            try:
                date = driver.find_element(By.XPATH,
                                           '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[3]/div[1]/div[1]').text.strip(
                    "Date of Conference: ")
            except:
                date = ''
            print("\tDate of Publication:", date)

            # abstract__________________________________________________________________________________________________
            abstract = ''
            try:
                abstract = driver.find_element(By.XPATH,
                                               '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[1]/div/div/div').text
            except:
                abstract = ''
            print("\tabstract:", abstract)

            # Published in______________________________________________________________________________________________
            published = {}
            try:
                published_name = driver.find_element(By.XPATH,
                                                     '//*[@id="xplMainContentLandmark"]/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[2]/a')
                published_link = published_name.get_attribute('href')
                published = {
                    "name": published_name.text,
                    "link": published_link
                }
            except:
                published = {}
            print("\tPublished in:", published)

            # Authors___________________________________________________________________________________________________
            authors = []
            try:
                authors_button = driver.find_element(By.XPATH,
                                                     '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/xpl-accordian-section/div/xpl-document-accordion/div[1]/div[1]/button')
                authors_button.click()
                authors_parent = driver.find_element(By.XPATH,
                                                     '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/xpl-accordian-section/div/xpl-document-accordion/div[1]/div[2]')
                authors_children = authors_parent.find_elements(By.XPATH, './*')
                for author in authors_children:
                    author_name = author.find_element(By.XPATH, './xpl-author-item/div/div[1]/div/div[1]/a/span').text
                    author_form = author.find_element(By.XPATH, './xpl-author-item/div/div[1]/div/div[2]/div').text
                    authors.append({
                        "name": author_name,
                        "from": author_form
                    })
            except:
                authors = []
            print("\tAuthors:", authors)

            # IEEE Keywords and Author Keywords_________________________________________________________________________
            ieee_keywords = []
            author_keywords = []
            try:
                keywords_button = driver.find_element(By.XPATH,
                                                      '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/xpl-accordian-section/div/xpl-document-accordion/div[5]/div[1]/button')
                keywords_button.click()
                ieee_keywords_parent = driver.find_element(By.XPATH,
                                                           '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/xpl-accordian-section/div/xpl-document-accordion/div[5]/div[2]/xpl-document-keyword-list/section/div/ul/li[1]/ul')
                ieee_keywords_children = ieee_keywords_parent.find_elements(By.XPATH, './*')
                for ieee_keyword in ieee_keywords_children:
                    ieee_keyword_name = ieee_keyword.find_element(By.XPATH, './a').text
                    ieee_keywords.append(ieee_keyword_name)
                author_keywords_parent = driver.find_element(By.XPATH,
                                                             '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/xpl-accordian-section/div/xpl-document-accordion/div[5]/div[2]/xpl-document-keyword-list/section/div/ul/li[3]/ul')
                author_keywords_children = author_keywords_parent.find_elements(By.XPATH, './*')
                for author_keyword in author_keywords_children:
                    author_keyword_name = author_keyword.find_element(By.XPATH, './a').text
                    author_keywords.append(author_keyword_name)
            except:
                ieee_keywords = []
                author_keywords = []
            print("\tIEEE Keywords:", ieee_keywords)
            print("\tAuthor Keywords:", author_keywords)

            articles.append({
                "title": title,
                "Cites in Papers": papers,
                "Cites in Patent": patent,
                "Full Text Views": views,
                "Publisher": publisher,
                "DOI": doi,
                "Date of Publication": date,
                "abstract": abstract,
                "Published in": published,
                "Authors": authors,
                "IEEE Keywords": ieee_keywords,
                "Author Keywords": author_keywords
            })

            driver.get(back_url)

        WebDriverWait(driver, 120).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, f'stats-Pagination_{i + 1}'))
        )

        next_button = driver.find_element(By.CLASS_NAME, f'stats-Pagination_{i + 1}')
        next_button.click()

        WebDriverWait(driver, 120).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-search-results/div/div[2]/div[2]/xpl-results-list/div[27]/xpl-results-item/div[1]/div[1]/div[2]/h3/a'))
        )
    with open(f'{sort}.json', 'w') as json_file:
        json.dump(articles, json_file, indent=4)
    return articles


relevance = crawl_ieee_xplore("relevance")
newest = crawl_ieee_xplore("newest")
result = [relevance, newest]
with open('IEEE_result.csv', 'w') as result_file:
    json.dump(result, result_file, indent=4)