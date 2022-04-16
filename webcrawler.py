# 要引入才能用
import json, bs4, random, time, requests
# ptt domain name
domain = "https://www.ptt.cc"
# ptt route 換頁用
route = "/bbs/AngelPray/index.html"
# ptt jsonList 給jsonfile存檔用
jsonList = []
# 爬個約200筆左右
for i in range(10):
    # 把url組合起來
    response = requests.get(domain + route)
    # BeautifulSoup解析
    result = bs4.BeautifulSoup(response.text, 'html.parser')
    # ptt的標題們在r-ent元素
    article = result.find_all('div', class_ = 'r-ent')
    for j in article:
        jsonDict = {}
        title = j.find('a').text
        author = j.find('div', class_ = 'author').text
        timestamp = j.find('div', class_ = 'date').text
        url = domain + j.a['href']
        # 印出標題 作者 發文時間 網址
        print("標題=>", title)
        print("作者=>", author)
        print("發文時間=>", timestamp)
        print("網址=>", url)
        print("---------------------------------------------")    
        # 把值塞進jsonDict
        jsonDict["標題"] = title
        jsonDict["作者"] = author
        jsonDict["發文時間"] = timestamp
        jsonDict["網址"] = url    
        jsonList.append(jsonDict)   
    # ptt的換頁在btn wide元素
    next = result.find_all('a', class_ = 'btn wide')
    # 取得route
    route = next[1].get('href')
    # 爬蟲會隨機休息1至10秒模擬人類
    time.sleep(random.uniform(1, 10))
# 存成json檔
with open('Saved.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(jsonList, jsonfile)

