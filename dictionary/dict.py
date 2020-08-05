book = {2018:['Educated','becoming','the outsider'], 2019:['The silent patient','the testmate']}
for years in book.keys():
    print(f'{years}')
for books in book.values():
    print(f'{books}')
for years,books in book.items():
    print(f'Published in {years}: {book}')

print(book.get(2019))
book[2019]