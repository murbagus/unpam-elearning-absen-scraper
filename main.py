from bs4 import BeautifulSoup
from login import getPage

# Input url
url = input('Masukan URL (topik forum diskusi): ')
username = input('Masukan username: ')
password = input('Masukan password: ')

# Ambil para author posting di forum
print('')
print('Mulai scraping...')
page = getPage(url, username, password)
bsObj = BeautifulSoup(page, features='html.parser')

print('Mengambil author...')
print('')
print('=============================================================')
author_discussion = []
authors = bsObj.findAll('div', {'class': 'author'})
for author in authors:
    x = author.find('a').get_text()
    # if x not in author_discussion:
    #     author_discussion.append(x)
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
for author in sorted(author_list, key=lambda i: i['nama']):
    print('>> ' + author['nama'] +
          '\t\t (aktif: ' + str(author['jumlah_aktif']) + ')')

print('=============================================================')
print('')

print('Ada ' + str(len(author_list)) + ' mahasiswa berdisksusi')
