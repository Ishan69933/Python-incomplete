import requests
from bs4 import BeautifulSoup as bs

URL  = "https://www.amazon.in/Nitho-Racing-MLT-DP16-K-Compatible-Switch/dp/B08LFLHXGC/ref=sr_1_10?crid=324D91VTZB1WZ&keywords=steering%2Bwheel&qid=1696227331&sprefix=steering%2Bwhee%2Caps%2C625&sr=8-10&th=1"

page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"})

soup = bs(page.content, "html.parser")
print(soup.find(id = "priceblock_ourprice"))