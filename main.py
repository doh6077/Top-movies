from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.secret_key= 'adsadsadasdsadsadsadsadsadsadsakjgjdskl'
bootstrap=Bootstrap(app)

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




# Define Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

class MovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g.7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField('Submit')
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

with app.app_context():
    db.create_all()
    if not Movie.query.first():
        # Add initial movie
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()

@app.route("/",methods=['GET','POST'])
def home():

    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/update/<id>",methods=['GET','POST'])
def update(id):
    movie = Movie.query.filter_by(id=id).first()
    print(f"This is movie info{movie}")
    form = MovieForm(obj=movie)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form =form)

@app.route("/delete/<id>",methods=['GET','POST'])
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/detail/<movie_id>",methods=['GET','POST'])
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYjJlMWMyMTdmOGY5NzdmZGY4NjdhNjkxNmFiMzQ2MSIsInN1YiI6IjY2MzgyZDZkYjc2Y2JiMDEyNjYyMmU2OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aE1mbVu3Qea898Xkux_ZrDp2lyjkD2kgiEyDch_9po8"
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    print(data)
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split("-")[0],
        description=data['overview'],
        rating=None,
        ranking=None,
        review="None",
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    movie = Movie.query.filter_by(title=data['title']).first()

    return redirect(url_for("update", id=movie.id))

@app.route("/add",methods=['GET','POST'])
def add():
    form = FindMovieForm()

    if form.validate_on_submit():
        # Extract the query from the form data after form submission
        query = form.title.data

        # API configuration 
        url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYjJlMWMyMTdmOGY5NzdmZGY4NjdhNjkxNmFiMzQ2MSIsInN1YiI6IjY2MzgyZDZkYjc2Y2JiMDEyNjYyMmU2OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aE1mbVu3Qea898Xkux_ZrDp2lyjkD2kgiEyDch_9po8"
        }
        
        response = requests.get(url, headers=headers)
        data = response.json()
        return render_template("select.html", data=data)
    
    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
