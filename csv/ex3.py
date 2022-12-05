# ex3

import usecsv, os, re
import usecsv as uc

os.chdir(r".\data")

apt = uc.switch(uc.opencsv("apt_202210.csv"))

new_list = []
for i in apt :
    try :
        # 부산 크기는 150넘거나 거래금액 5억 이상인 조건
        if (i[5] >= 150 or i[-7] >= 50000) and re.match("부산", i[0]) :
            print(i[0], i[4], i[-4])
            new_list.append([i[0], i[4], i[-4]])
    except :
        pass

print(len(new_list))
uc.writecsv("over150+high50000.csv", new_list)