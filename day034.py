import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
print(HTML)
URLS = HTML.splist('\n')
for url in URLS:
    cd = url.split(';')[-1]
    response = requests.get(url)
    content = response.content
    with open(cd,'wb') as f:
       f.write(content)






