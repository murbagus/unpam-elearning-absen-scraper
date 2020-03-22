from bs4 import BeautifulSoup
from login import getPage

# Input url
url = input('Masukan URL: ')
username = input('Masukan username: ')
password = input('Masukan password: ')

# Ambil para kreator posting di forum
print('')
print('Mulai scraping...')
page = getPage(url, username, password)
bsObj = BeautifulSoup(page, features='html.parser')

print('Mengambil author...')
print('')
print('=============================================================')
author_list = []
authors = bsObj.findAll('div', {'class': 'author'})
for author in authors:
    x = author.find('a').get_text()
    if x not in author_list:
        author_list.append(x)

# Hapus author pertama karena merupakan dosen
author_list.pop(0)
# Print author ascending
author_list.sort()
for author in author_list:
    print('>> ' + author)

print('=============================================================')
print('')

print('Ada ' + str(len(author_list)) + ' mahasiswa berdisksusi')
