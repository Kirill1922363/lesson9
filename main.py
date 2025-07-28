from flask import Flask, render_template, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Coming-of-age"},
    {"id": 6, "title": "To the Lighthouse", "author": "Virginia Woolf", "genre": "Modernist"},
    {"id": 7, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "genre": "Gothic"},
    {"id": 8, "title": "The Adventures of Sherlock Holmes", "author": "Arthur Conan Doyle", "genre": "Detective"},
    {"id": 9, "title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"id": 10, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy"}
]


@app.route("/")
def index():
    return "<h1>Hello user!!!</h1>"

@app.route('/books/')
def all_books():
    book_list = ""
    for book in books:
        book_list += f"<p>{book["id"]}: <strong>{book['title']}: Author {book["author"]}</strong> in genre {book["genre"]}</p>"
    return f"<h1>Список книг</h1><div>{book_list} </div>"


@app.route('/books/<int:id_book>/')
def book(id_book:int):
    book = next((book for book in books if book["id"] == id_book), None)
    if book:
        return f"<h1>selected book:</h1><p> <strong>{book['title']}: Author {book["author"]}</strong> in genre {book["genre"]}</p>"
    return f"<h1>такої книги немає</h1>", 404


@app.route("/api/books/")
def book_api():
    return jsonify({"books": books})

@app.route('/genres/')
def get_genres():
    unique_genres = []
    for book in books:
        if book['genre'] not in unique_genres:
            unique_genres.append(book['genre'])
    
    genre_list = ""
    for genre in unique_genres:
        genre_list += f"<p><strong>{genre}</strong></p>"
    
    return f"<h1>Список жанрів</h1><div>{genre_list}</div>"

if __name__ == "__main__":
    app.run(debug=True)
