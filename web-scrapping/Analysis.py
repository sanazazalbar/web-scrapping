import csv

books = []

with open("all_books.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        books.append(row)

for book in books:
    book["price"] = float(book["price"].replace("£", ""))

    
rating_map = {
    "One stars": 1,
    "Two stars": 2,
    "Three stars": 3,
    "Four stars": 4,
    "Five stars": 5
}

for book in books:
    book["rating"] = rating_map[book["rating"]]
    
#AVERAGE PRICE
total_price = 0

for book in books:
    total_price += book["price"]

avg_price = total_price / len(books)
print("Average Price:", avg_price)

total_rating = 0

#AVERAGE RATING
for book in books:
    total_rating += book["rating"]

avg_rating = total_rating / len(books)
print("Average Rating:", avg_rating)

#MOST EXPENSIVE BOOKS
max_book = books[0]

for book in books:
    if book["price"] > max_book["price"]:
        max_book = book

print("Most Expensive Book:", max_book)

#CHEAPEST BOOK
min_book = books[0]

for book in books:
    if book["price"] < min_book["price"]:
        min_book = book

print("Cheapest Book:", min_book)



