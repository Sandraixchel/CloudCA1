from flask import Flask, jsonify, request, render_template, redirect
app = Flask(__name__)

movies = [
  {
    "id": 1,
    "title": "After Sun",
    "director": "Charlotte Wells",
    "gender": "Drama",
    "year" : "2022",
    "description": "Twenty years after their last holiday at a fading vacation resort, Sophie reflects on the rare time spent with her loving and idealistic father Calum. At 11-years-old, as the world of adolescence creeps into Sophie's view, Calum struggles under the weight of life outside of fatherhood.",
    "rotten": "96%",
    "price": 5.99 
    
    
    
  },
  {
    "id": 2,
    "title": "Inception",
    "director": "Christopher Nolan",
    "gender": "Science Fiction",
    "year" : "2010",
    "description":"Cobb steals information from his targets by entering their dreams. Saito offers to wipe clean Cobb's criminal history as payment for performing an inception on his sick competitor's son.",
    "rotten":"87%",
    "price": 3.99 
  },
   {
    "id": 3,
    "title": "The Whale",
    "director": "Darren Aronofsky",
    "gender": "Psychological Drama",
    "year" : "2022",
    "description":"In a town in Idaho, Charlie, a reclusive and unhealthy English teacher, hides out in his flat and eats his way to death. He is desperate to reconnect with his teenage daughter for a last chance at redemption.",
    "rotten":"64%",
    "price": 4.50 
  },
   {
    "id": 4,
    "title": "Django",
    "director": "Quentin Tarantino",
    "gender": "Western/Drama",
    "year" : "2013",
    "description":"When Django, a slave, is freed, he joins forces with a bounty hunter to rescue his wife, who has been enslaved by Calvin, a hard-hearted plantation owner.",
    "rotten":"87%",
    "price": 2.99 
  },
   {
    "id": 5,
    "title": "Nope",
    "director": "Jordan Peele",
    "gender": "Horror/Sci-fi",
    "year" : "2022",
    "description":"A man and his sister discover something sinister in the skies above their California horse ranch, while the owner of a nearby theme park tries to profit from the mysterious, otherworldly phenomenon.",
    "rotten":"83%",
    "price": 5.99 
  },
   {
    "id": 6,
    "title": "Triangle of Sadness",
    "director": "Ruben Östlund",
    "gender": " Drama/Comedy ",
    "year" : "2022",
    "description":"Carl and Yaya, a couple of influencers, are invited to a luxury cruise ship alongside a group of out of touch wealthy people. The situation takes an unexpected turn when a brutal storm hits the ship.",
    "rotten":"72%",
    "price": 1.99 
  },
  {
    "id": 7,
    "title": "The Dark Knight",
    "director": "Christopher Nolan",
    "gender": "Action/Adventure",
    "year" : "2008",
    "description":"After Gordon, Dent and Batman begin an assault on Gotham's organised crime, the mobs hire the Joker, a psychopathic criminal mastermind who offers to kill Batman and bring the city to its knees.",
    "rotten":"94%",
    "price": 6.99 
  },
  {
    "id": 8,
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "gender": "Sci-fi/Adventure ",
    "year" : "2014",
    "description":"When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
    "rotten":"73%",
    "price": 6.99 
  },
  {
    "id": 9,
    "title": "Gravity",
    "director": "Alfonso Cuarón",
    "gender": " Sci-fi/Thriller",
    "year" : "2013",
    "description":"On an outer space mission, engineer Ryan Stone and astronaut Matt Kowalski are hit by high-speed space debris. As the situation gets dire, Stone rises to the occasion as a survivor.",
    "rotten":"96%",
    "price": 7.99 
  },
  {
    "id": 10,
    "title": "Armageddon",
    "director": "Michael Bay",
    "gender": "Sci-fi/Action",
    "year" : "1998",
    "description":"After discovering that an asteroid the size of Texas will impact Earth in less than a month, NASA recruits a misfit team of deep-core drillers to save the planet.",
    "rotten":"38%",
    "price": 2.99 
  },
  {
    "id": 11,
    "title": "Pan's Labyrinth",
    "director": "Guillermo Del Toro",
    "gender": "Fantasy/War",
    "year" : "2006",
    "description":"Ofelia moves with her mother to her stepfather's house. At night, a fairy leads her to a faun who informs her that she is a princess and she needs to participate in three tasks to prove her royalty.",
    "rotten":"95%",
    "price": 5.99 
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
        return render_template('getInfo.html', movie = movie)
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
  new_description = request.form['description']
  new_rotten = request.form['rotten']
  new_price = float(request.form['price'])
  new_movie = {"id": new_id, "title": new_title, "director": new_director, "gender": new_gender, "year": new_year, new_description: "description", new_rotten: "rotten", "price": new_price }
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

