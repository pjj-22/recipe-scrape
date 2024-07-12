import cloudscraper
from bs4 import BeautifulSoup

url = "https://www.budgetbytes.com/easy-lemon-pepper-chicken/"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

ingredients_section = soup.find('div', class_='wprm-recipe-ingredients-container')
ingredients = [li.get_text(strip=True) for li in ingredients_section.find_all('li')]

instructions_section = soup.find('div', class_='wprm-recipe-instructions-container')
instructions = [li.get_text(strip=True) for li in instructions_section.find_all('li')]

print(ingredients)

print(instructions)
