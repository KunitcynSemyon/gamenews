import requests
from bs4 import BeautifulSoup as bs



def stopgame_parser(requests):
	headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
           }

	baseUrl = 'https://stopgame.ru/articles/new'
	session = requests.Session()
	data_stopgame = []
	requests = session.get(baseUrl, headers = headers)
	if requests.status_code == 200:
		soup = bs(requests.content, 'html.parser')
		divs = soup.find_all('div', attrs={'class': 'caption caption-bold'})
		for div in divs:
			title = div.find('a').text
			href = div.find('a')['href']
			data_stopgame.append({
            	'title' : title,
                'href' : 'https://stopgame.ru' + str(href),
            })
	else:
		print('Error')
	return data_stopgame