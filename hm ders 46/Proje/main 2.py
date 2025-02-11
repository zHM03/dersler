books = [
    {"title": "1984", "author": "george orwell", "year": 1949},
    {"title": "to kill a mockingbird", "author":"harper lee", "year": 1960},
    {"title": "the great gatsby", "author": "f, scot fitzgerald", "year": 1925},
]
#sıralama
books_sorted_by_title = sorted(books, key=lambda x: x["title"])
print("başlığa göre sıralanmış kitaplar:", books_sorted_by_title)

#arama
def search_book(title):
    for book in books:
        if book["title"] == title:
            return book
        return None
print("aranan kitap:", search_book("1984"))