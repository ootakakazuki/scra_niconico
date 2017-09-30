from bs4 import BeautifulSoup
import requests

inp = input("検索したい文字を入れよう")
url = "http://www.nicovideo.jp/ranking/fav/daily/g_other"
HTML = requests.get(url)
soup = BeautifulSoup(HTML.content, "html.parser")
div = soup.find_all("div", {"class": "column main"})
c = 0
for i in div:
    b = i.find_all("a")
    for num, d in enumerate(b):
        if num % 4 == 1:  # num は語録を抜き取る用のインデックス
            c += 1 # カウンター。ランキングを表す
            if c <= 9:
                if str(d.string).find(inp) != -1:
                    print("No.0"+str(c), d.get_text().encode("cp932", "ignore").decode("cp932"))
            else:
                if str(d.string).find(inp) != -1: 
                    print("No."+str(c), d.get_text().encode("cp932", "ignore").decode("cp932"))

