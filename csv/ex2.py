# ex2

import usecsv, os, re
import usecsv as uc

os.chdir(r".\data")

apt = uc.switch(uc.opencsv("apt_202210.csv"))

# for i in apt[:6] :
#     print(i[-7])

# print("거래개수 " , len(apt))

new_list = []
for i in apt :
    try :
        # 강원도 크기는 120넘고 거래금액 3억 이상인 조건
        if i[5] >= 120 and i[-7] <= 300000 and re.match("강원", i[0]) :
            # print(i[0], i[4], i[-4])
            new_list.append([i[0], i[4], i[-4]])
    except :
        pass

print(len(new_list))
uc.writecsv("over120_lower30000.csv", new_list)