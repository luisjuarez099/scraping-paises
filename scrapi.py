import requests
from bs4 import BeautifulSoup

# URL de la página a analizar
url = 'https://www.cyberpuerta.mx/Computadoras/PC-s-de-Escritorio/'

# Obtener la página
page = requests.get(url)

# Analizar la página con BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Encontrar los productos y sus descuentos
products = soup.find_all('div', class_='product-item')

# Imprimir la información de cada producto
for product in products:
    # Obtener el nombre del producto
    name = product.find('h3', class_='product-title').text.strip()
    
    # Obtener el precio original
    original_price = product.find('div', class_='price-old').text.strip()
    
    # Obtener el precio con descuento
    discount_price = product.find('div', class_='price-new').text.strip()
    
    # Obtener el porcentaje de descuento
    discount_percent = product.find('span', class_='discount').text.strip()
    
    # Imprimir la información del producto
    print(name)
    print('Precio original:', original_price)
    print('Precio con descuento:', discount_price)
    print('Porcentaje de descuento:', discount_percent)
    print()