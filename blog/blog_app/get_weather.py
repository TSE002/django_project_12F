import requests
from bs4 import BeautifulSoup

def getData():
	url = "https://www.idokep.hu/idojaras/Budapest"
	page = requests.get(url)
	code = BeautifulSoup(page.text, "html.parser")
	kep = code.findAll('img', attrs={'class': 'ik forecast-bigicon pr-2 pd-md-0'})[0]
	kep_link = "https://www.idokep.hu" + kep['src']
	jelenleg = code.findAll('div', attrs={'class': 'ik current-weather'})[0]
	jelenleg_szoveg = jelenleg.contents[0]
	homerseklet = code.findAll('div', attrs={'class': 'ik current-temperature'})[0]
	homerseklet = homerseklet.contents[0].rstrip()
	vissza = [kep_link, jelenleg_szoveg, homerseklet]
	return vissza