"""
简单的Web抓取
"""
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.title.string
print(f"Page title: {title}")
