from bs4 import BeautifulSoup
import requests

file_path = '/index.html'
response = requests.get('file://' + file_path)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

def test():
    doll = 1 + 1