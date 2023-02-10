import requests 
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as mtl

labels=['name','capital','poblacion']
def scrap_bok():
	paises=[]
	noms=[]
	pops=[]
	markup=requests.get(f'https://www.scrapethissite.com/pages/simple/').text
	soup=BeautifulSoup(markup,'html.parser')
	#print(soup) #imprime todo el scrap de html
	for items in soup.find_all("div",{"class":"col-md-4 country"}):
		#print(items)
		countrys={}
		#paises nombre
		n=items.select_one("h3").get_text().strip()
		
		noms.append(n)
		countrys['name']=n

		#capitales
		c=items.select_one("span",{"class":"country-capital"}).get_text()
		#print(c)
		#countrys['capital']=c


		#poblacion
		p=items.find("span",{"class":"country-population"}).get_text()
		#print(p)
		p=int(p)
		#print(type(p))
		pops.append(p)
		countrys['poblacion']=p
		#print(countrys)
		paises.append(countrys)
		#print(paises)
	names=[]
	pop=[]
	#filtramos la poblacion menor que  diez mil
	ranks=list(filter(lambda i:i['poblacion']<10000 , paises))
	#print(ranks)
	#limpiamos para dividir en  listas los paises y su poblacion
	for i in ranks:
		#print(i)
		for j in i.values():
			if type(j)==str:
				names.append(j)
			elif type(j) == int:
				pop.append(j)
	#print(names)
	#print(pop)
	#graficamos con matplot
	mtl.figure(figsize=(11,5))
	mtl.bar(names,pop,align="center")
	mtl.xticks(rotation=90,size=7)
	mtl.show()
	

	
	#print(pop_rank)
	try:
		with open('countrys.csv','w') as f:
			writer = csv.DictWriter(f,fieldnames=labels)
			writer.writeheader()
			for i in paises:
				writer.writerow(i)
	except IOError:
		print("ERROr")


if __name__=='__main__':

	scrap_bok()