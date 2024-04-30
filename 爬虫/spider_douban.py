import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
urls=[
    "http://books.toscrape.com/",#爬虫练习网址
    "https://www.ceic.ac.cn/history",#地震局台网
    "https://www.letpub.com.cn/index.php?page=grant",#国自然科学基金查询
    "https://movie.douban.com/top250",#豆瓣电影top250
    ]

hrefs=[]
spans=[]
for start_num in tqdm(range(0,250,25)):
    # print(star_num)
    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"    }
    respones=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=custom_headers)
    #是否请求成功
    if respones.ok:
        pass
        # print('请求成功')
    else:
        print('请求失败')
    soup=BeautifulSoup(respones.text,"html.parser")#解析网页结构(使用bs4)
    all_a=soup.findAll("a",attrs={"class":""})#输入你想要的html元素和类
    for a in all_a:
        span=a.find("span")
        if span:
            spans.append(span.string)
            hrefs.append(a.get("href"))
            # print(span.string,a.get("href"))
print('生成完毕',f'共有{spans.__len__()}个电影被导出')
mvdist={index+1:value for index,value in enumerate(spans)}
filepath=r"C:\Users\sunka\Desktop\豆瓣Top250电影.md"
with open(filepath,'w',encoding='utf-8') as file:
    file.write("|排名 | 电影名 | 网址|\n")
    file.write(":-----: | :-----: |:-----:\n")
    for i,value in enumerate(spans):
        file.write(f'{i+1}|{value}|{hrefs[i]}\n')
    print(f'导出地址为{filepath}')