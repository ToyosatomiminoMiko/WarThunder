# -*- coding:UTF-8 -*-

#from lxml import etree
import bs4
import requests as re

urls = [
    "https://wiki.warthunder.com/Category:USA_ground_vehicles",
    "https://wiki.warthunder.com/Category:Germany_ground_vehicles",
    "https://wiki.warthunder.com/Category:USSR_ground_vehicles",
    "https://wiki.warthunder.com/Category:Britain_ground_vehicles",
    "https://wiki.warthunder.com/Category:Japan_ground_vehicles",
    "https://wiki.warthunder.com/Category:China_ground_vehicles",
    "https://wiki.warthunder.com/Category:Italy_ground_vehicles",
    "https://wiki.warthunder.com/Category:France_ground_vehicles",
    "https://wiki.warthunder.com/Category:Sweden_ground_vehicles",
]

countryallVlist = []

# 欺骗
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'}


def countryVlist(url):
    # 获取国家页面
    cVlist = re.get(url)
    soup = bs4.BeautifulSoup(cVlist.text, features="lxml")
    # 提取标签
    cVlist_a = soup.find_all("div", "mw-category-group")
    cVlist_aList = list(cVlist_a)
    for tag in cVlist_aList:
        soup1 = bs4.BeautifulSoup(str(tag), features="lxml")
        cVlist_a_text = soup1.find_all("a")
        for tag0 in list(cVlist_a_text):
            # 提取文本
            cVlist_a_text = tag0.get('href')
            # 加入列表
            countryallVlist.append(cVlist_a_text)


for url in urls:
    countryVlist(url=url)

print(len(countryallVlist), '\n', '='*50)

'''
def main1():  # ①获取新数据
    pass


def main2():  # ②选择本地数据
    pass


def File():
    s = """
    选择模式：
    ①获取新数据
    ②选择本地数据
    """
    a = input(s)
    if a == "1":
        main1()
    elif a == "2":
        main2()
    else:
        print("请重新选择")
'''

url = "https://wiki.warthunder.com"


def vhtmlfun(vurl):
    global url
    # 请求
    r = re.get(url+vurl, headers=headers)
    soup = bs4.BeautifulSoup(r.text, features="lxml")
    # div class="specs_info"
    V_info = list(soup.find_all("div", "specs_char"))

    # 数据过滤

    #
    print("==="*50)
    print(V_info)
    print("END"*50)


for v_url in countryallVlist:

    vhtmlfun(v_url)
'''
if __name__ == "__main__":
    File()
'''
