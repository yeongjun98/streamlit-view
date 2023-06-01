#필요_라이브러리
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

JNU_url="https://www.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=5&cate=5"
html=urllib.request.urlopen(JNU_url)
soupJNU=BeautifulSoup(html,'html.parser')

tag_tbody=soupJNU.find('tbody')
tag_tr=tag_tbody.find_all('tr')
tag_td=tag_tr[0].find_all('td')
href=tag_td[1].find("a")
result=[]
a=tag_td[0].string
url="https://www.jnu.ac.kr"
for notice in tag_tbody.find_all('tr'):
    notice_td=notice.find_all('td')
    notice_date=notice_td[3].string #날짜정보
    notice_name=notice_td[1].string #제목정보
    notice_href=url+notice_td[1].find("a").attrs["href"]#href
    result.append([notice_date,notice_name,notice_href])

JNU_tbl=pd.DataFrame(result,columns=('date','name','href'))
JNU_tbl["name"]=JNU_tbl["name"].str.replace("\xa0"," ")
print(JNU_tbl)

#csv 저장
path="C:/Users/Hyeon/Desktop/지식공학_project/"
JNU_tbl.to_csv(path+"JNU_notice.csv",encoding="cp949",index=True)