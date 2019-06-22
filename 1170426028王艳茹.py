import requests
url = ' <a target="_blank" href="/s?wd=%E7%A1%AC%E7%9B%98%E8%93%9D%E7%9B%98&ie=utf-8&rsv_cq=&rsv_dl=0_right_recommends_merge_21102&amp;euri=3cbddd1068e046e48faaa32e15d7cc34"><img data-src="http://t11.baidu.com/it/u=1809028495,1785840528&fm=58" data-b64-id="1809028495_1785840528_58" class="c-img c-img4 opr-recommends-merge-img"/></a>'
response = requests.get(url)
HTML = response.text
print(HTML)
res = url.split(';')
for href in res:
    if 'href' in url:
        print(res[0])