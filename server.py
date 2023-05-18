from flask import Flask, jsonify, request, render_template, redirect
app = Flask(__name__)

books = [
  {
    "id": 1,
    "title": "Becoming",
    "author": "Michelle Obama",
    "price": 22.99 
  },
  {
    "id": 2,
    "title": "Humans of New York",
    "author": "Brandon Stanton",
    "price": 19.99 
  }  
]

#curl http://localhost:5000
@app.get('/')
def index():
  return render_template('index.html', data = books)

#curl http://localhost:5000/books
@app.get('/books')
def hello():
  return jsonify(books)

#curl http://localhost:5000/book/1
@app.get('/book/<int:id>')
def get_book(id):
  for book in books:
    if book["id"] == id:
        return jsonify(book)
  return f'Book with id {id} not found', 404

#curl http://localhost:5000/add_book --request POST --data '{"id":3,"author":"aaa","title":"bbb","price":99.99}' --header "Content-Type: application/json"
@app.post("/add_book")
def add_book():
  #data = request.get_json()
  new_id = int(request.form['id'])
  new_title = request.form['title']
  new_author = request.form['author']
  new_price = float(request.form['price'])
  new_book = {"id": new_id, "title": new_title, "author": new_author, "price": new_price }
  books.append(new_book)
  return redirect('/')
  

#curl http://localhost:5000/update_book/2 --request POST --data '{"author":"ccc","title":"ddd","price":999.99}' --header "Content-Type: application/json"
@app.route('/update_book/<int:id>', methods=['GET','POST'])
def update_book(id):  
  for book in books:
    if book["id"] == id:
        if request.method=="POST":
          book["id"] = int(request.form['id'])
          book["title"] = request.form['title']
          book["author"] = request.form['author']
          book["price"] = float(request.form['price'])
          return redirect('/')
        else:
          return render_template('update.html', book = book)
  return f'Book with id {id} not found', 404

#curl http://localhost:5000/delete_book/1 --request DELETE
@app.route('/delete_book/<int:id>', methods=['GET','POST'])
def delete_book(id):
  for book in books:
    if book["id"] == id:
        if request.method=="POST":
          books.remove(book)
          return redirect('/')
        else:
          return render_template('delete.html', book = book)
  return f'Book with id {id} not found', 404

