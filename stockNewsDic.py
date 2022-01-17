def pyETLSeekingAlphaNews(stock):

    import requests
    import json
    import datetime

    userAgent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'

    #取得User-Agent資格
    headers = {
        #User-Agent固定寫法
        'User-Agent': userAgent
    }

    today= datetime.date.today()
    # stock = str(input('輸入股票代碼:'))
    # url = 'https://seekingalpha.com/symbol/NVDA/news?from=2021-12-01&to=2021-12-30'
    url = 'https://seekingalpha.com/api/v3/symbols/{}/news?cacheBuster={}&filter[since]=0&id=tsla&page[size]=5&page[number]=1'.format(stock, today)

    ss = requests.session()
    res = ss.get(url, headers=headers)

    jsonData = json.loads(res.text) # list of article object

    article_URL_Dic = {}
    for attributes in jsonData['data']:
        article_URL_Dic.setdefault(attributes['attributes']['title'], 'https://seekingalpha.com/news/' + (attributes['links']['self'])[6:13])
        # print(attributes['attributes']['title'])
        # print('https://seekingalpha.com/api/v3/news/' + (attributes['links']['self'])[6:13])
    # print(article_URL_Dic)

    result=''
    page=1
    for singleAriticle in article_URL_Dic:
        # print(page)
        result += str(page)
        result += '\n'
        # print(singleAriticle) #print title
        # result += singleAriticle
        # result += '\n'
        singleArtUrl = article_URL_Dic.get(singleAriticle)
        # print(singleArtUrl)  # print URL
        result += singleArtUrl
        result += '\n'
        page += 1

    # print(type(result))
    return result
