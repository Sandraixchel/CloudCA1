from flask import Flask, jsonify, request, render_template, redirect
app = Flask(__name__)

movies = [
  {
    "id": 1,
    "title": "Becoming",
    "director": "Michelle Obama",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
  {
    "id": 2,
    "title": "Inception",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
   {
    "id": 3,
    "title": "Barbie",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
   {
    "id": 4,
    "title": "Super Mario",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
   {
    "id": 5,
    "title": "Batman",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
   {
    "id": 6,
    "title": "From",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
  {
    "id": 7,
    "title": "From",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
  {
    "id": 8,
    "title": "From",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
  {
    "id": 9,
    "title": "From",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
  {
    "id": 10,
    "title": "From",
    "director": "C. Nolan",
    "gender": "Drama",
    "year" : "2010",
    "price": 22.99 
  },
  
  {
    "id": 3,
    "title": "Humans of New York",
    "author": "Brandon Stanton",
    "price": 19.99 
  },
  
]

#curl http://localhost:5000
@app.get('/')
def index():
  return render_template('index.html', data = movies)

#curl http://localhost:5000/movies
@app.get('/movies')
def hello():
  return jsonify(movies)

#curl http://localhost:5000/movie/1
@app.get('/movie/<int:id>')
def get_movie(id):
  for movie in movies:
    if movie["id"] == id:
        return jsonify(movie)
  return f'Movie with id {id} not found', 404

#curl http://localhost:5000/add_movie --request POST --data '{"id":3,"director":"aaa","title":"bbb", "gender":"ccc", "year": "ddd", price":99.99}' --header "Content-Type: application/json"
@app.post("/add_movie")
def add_movie():
  #data = request.get_json()
  new_id = int(request.form['id'])
  new_title = request.form['title']
  new_director = request.form['director']
  new_gender = request.form['gender']
  new_year = request.form['year']
  new_price = float(request.form['price'])
  new_movie = {"id": new_id, "title": new_title, "director": new_director, "gender": new_gender, "year": new_year, "price": new_price }
  movies.append(new_movie)
  return redirect('/')
  

#curl http://localhost:5000/update_movie/2 --request POST --data '{"id":3,"director":"aaa","title":"bbb", "gender":"ccc", "year": "ddd", price":99.99}' --header "Content-Type: application/json"
@app.route('/update_movie/<int:id>', methods=['GET','POST'])
def update_movie(id):  
  for movie in movies:
    if movie["id"] == id:
        if request.method=="POST":
          movie["id"] = int(request.form['id'])
          movie["title"] = request.form['title']
          movie["director"] = request.form['director']
          movie["gender"] = request.form['gender']
          movie["year"] = request.form['year']
          movie["price"] = float(request.form['price'])
          return redirect('/')
        else:
          return render_template('update.html', movie = movie)
  return f'Movie with id {id} not found', 404

#curl http://localhost:5000/delete_movie/1 --request DELETE
@app.route('/delete_movie/<int:id>', methods=['GET','POST'])
def delete_movie(id):
  for movie in movies:
    if movie["id"] == id:
        if request.method=="POST":
          movies.remove(movie)
          return redirect('/')
        else:
          return render_template('delete.html', movie = movie)
  return f'Movie with id {id} not found', 404

