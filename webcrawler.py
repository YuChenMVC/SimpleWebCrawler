# 要引入才能用
import bs4, random, time, requests
# ptt domain name
domain = "https://www.ptt.cc"
# ptt route 換頁用
route = "/bbs/AngelPray/index.html"
# 爬個約200筆左右 有時間再改成json版
for i in range(10):
    # 把url組合起來
    response = requests.get(domain + route)
    # BeautifulSoup解析
    result = bs4.BeautifulSoup(response.text, 'html.parser')
    # ptt的標題們在r-ent元素
    article = result.find_all('div', class_ = 'r-ent')
    for j in article:
        # 印出標題 作者 發文時間 網址
        print("標題=>", j.find('a').text)
        print("作者=>", j.find('div', class_ = 'author').text)
        print("發文時間=>", j.find('div', class_ = 'date').text)
        print("網址=>", domain + j.a['href'])
        print("---------------------------------------------")
    # ptt的換頁在btn wide元素
    next = result.find_all('a', class_ = 'btn wide')
    # 取得route
    route = next[1].get('href')
    # 爬蟲會隨機休息1至10秒模擬人類
    time.sleep(random.uniform(1, 10))


    