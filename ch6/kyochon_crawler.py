import time

from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd

def getData() :
    citys = ["", "서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
    result = []
    for sido1 in range(1, len(citys) + 1):
        try :
            print("현재 도시 : %s" % (citys[sido1]))
            print("작업 진행 : ", end="")
            for sido2 in range(1, 50):
                try :
                    url = "http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s" % (sido1, sido2)
                    html = urllib.request.urlopen(url)
                    soup = bs(html, "html.parser")
                    places = soup.select('span.store_item > strong')
                    for place in places :
                        result.append([citys[sido1]] + [place.string])
                    print("%d " %(sido2), end="")
                except :
                    print("다음 지역으로 넘어갑니다...")
                    break
        except :
            print("모든 지역의 매장위치 검색완료.")
            break

    return result

def main() :
    result = getData()
    # print(result)
    cb_tbl = pd.DataFrame(result, columns=["city", "place"])
    cb_tbl.to_csv("./data/kyochon_store.csv", encoding="utf-8", mode="w", index=True)
    print("파일 저장완료.")

if __name__ == "__main__" :
    main()
