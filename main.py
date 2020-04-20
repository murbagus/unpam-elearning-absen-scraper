from bs4 import BeautifulSoup
from login import getPage
from prettytable import PrettyTable
from dotenv import load_dotenv
import os

load_dotenv()

# Jumlah url
jumlah_topik = int(input('Jumlah topik diskusi: '))

# Input url
urls = []
for x in range(jumlah_topik):
    url_x = input('Masukan URL (topik forum diskusi): ')
    urls.append(url_x)
    # url = input('Masukan URL (topik forum diskusi): ')

# Meminta username dan password
username = os.getenv('USER_NAME') or input('Masukan username (dosen): ')
password = os.getenv('PASSWORD') or input('Masukan password (dosen): ')

# Ambil para author posting di forum
print('')
print('>> Mulai scraping...')

author_discussion = []
# Looping scraping setiap url
for i, url in enumerate(url):
    page = getPage(url, username, password)
    bsObj = BeautifulSoup(page, features='html.parser')

    print('>> Mengambil author forum ke ' + i + '...')
    print('')

    authors = bsObj.findAll('div', {'class': 'author'})
    for author in authors:
        x = author.find('a').get_text()
        author_discussion.append(x)

# Group nama author menjadi satu (tidak ada yang lebih dari satu)
author_list = []
for author in author_discussion:
    # Hitung jumlah aktif
    aktif = author_discussion.count(author)
    if not any(x.get('nama') == author for x in author_list):
        author_list.append({'nama': author, 'jumlah_aktif': aktif})

# Hapus author pertama karena merupakan dosen
author_list.pop(0)
# Print author ascending
pretty_table = PrettyTable(['Nama', 'Aktif'])
pretty_table.align['Nama'] = 'l'
for author in sorted(author_list, key=lambda i: i['nama']):
    pretty_table.add_row([author['nama'], author['jumlah_aktif']])

print(pretty_table)

print('')
print('>> Ada ' + str(len(author_list)) + ' mahasiswa berdisksusi')
