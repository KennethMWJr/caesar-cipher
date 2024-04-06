from bs4 import BeautifulSoup
import requests

file_path = '/index.html'
response = requests.get('file://' + file_path)
html_content = response.text
with open(file_path, 'r') as file:
    html_content = file.read()

#Create a Beautiful Soup object
soup = BeautifulSoup(html_content, 'html.parser')

def caesar(message, key, type):
    message = soup.select('#value').upper()
    key = soup.select('#key')
    type = soup.find_all('button')
    translated = ''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in message:
        templetter = letters.find(i)
        if type == soup.select('#encrypt'):
            templetter += key
            print('encrypt')
        elif type == soup.select('#decrypt'):
            templetter -= key
            print('decrypt')
        translated += letters[templetter]
    return translated
caesar()

print('test')
