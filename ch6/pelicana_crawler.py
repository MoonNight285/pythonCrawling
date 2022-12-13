

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

def getData() :
    result = []
    for pageNumber in range(1, 500) :
        print("다음 지역으로 이동합니다..")
        url = "https://pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si=" %(pageNumber)
        # html = urllib.request.urlopen(url)
        # soup = bs(html, "html.parser")

        # 한글 깨져서 requests 라이브러리 사용
        req = requests.get(url)
        soup = bs(req.text, "html.parser")

        try :
            for storeIdx in range(0, 10) :
                storeInfo = re.split("\'", soup.select('td.t_center > a')[storeIdx].attrs['onclick'])
                storeName = storeInfo[5]
                storeTel = storeInfo[7]
                storeAddress = storeInfo[9]

                if storeName.endswith("지사") == True :
                    continue

                result.append([storeName] + [storeTel] + [storeAddress])
        except Exception as e:
            # print('Exception occurred while code execution: ' + repr(e))
            break

    print("모든 지역의 검색이 완료되었습니다.")
    return result

def main() :
    result = getData()
    # print(result)
    cb_tbl = pd.DataFrame(result, columns=["Name", "Tel", "Address"])
    cb_tbl.to_csv("./data/pelicana_store.csv", encoding="utf-8", mode="w", index=True)
    print("파일 저장완료.")

if __name__ == "__main__" :
    main()
