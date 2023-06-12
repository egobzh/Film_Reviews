from flask import render_template, redirect,url_for
from pathlib import Path
from . import app,db
from .forms import ReviewForm,FilmForm
from .models import Movie,Review
from werkzeug.utils import secure_filename

BASEDIR = Path(__file__).parent
UPLOAD_FOLDER = BASEDIR / 'static'/'images'


@app.route('/')
def index():
   movies = Movie.query.order_by(Movie.id.desc()).all()
   if len(movies)==0:
      return render_template('index (empty).html')
   else:
      return render_template('index.html',movies=movies)

@app.route('/reviews')
def reviews():
   reviews = Review.query.order_by(Review.created_date.desc()).all()
   return render_template('reviews.html',reviews=reviews)

@app.route('/delete_review/<int:id>')
def del_reviews(id):
   Review.query.filter_by(id=id).delete()
   db.session.commit()
   return redirect('/reviews')

@app.route('/movie/<int:id>',methods=["GET", "POST"])
def film(id):
   reviewForm = ReviewForm()
   film = Movie.query.filter_by(id=id).one()
   sr_r=0
   if len(film.reviews)==0:
      sr_r=0.0
   else:
      for i in film.reviews:
         sr_r+=int(i.score)
      sr_r=round(sr_r/len(film.reviews),1)
   if reviewForm.validate_on_submit():
      no = Review()
      no.name = reviewForm.name.data
      no.text = reviewForm.text.data
      no.score = reviewForm.score.data
      no.movie_id = id
      db.session.add(no)
      db.session.commit()
      return redirect(f"/movie/{id}")

   if len(film.reviews)==0:
      return render_template('movie (without reviews).html', film=film,sr=sr_r,form=reviewForm)
   else:
      return render_template('movie.html',film=film,sr=sr_r,form=reviewForm)

@app.route('/add_movie',methods=["GET", "POST"])
def add_film():
   form = FilmForm()
   if form.validate_on_submit():
      no = Movie()
      no.title = form.title.data
      no.description = form.description.data
      image = form.image.data
      image_name = secure_filename(image.filename)
      UPLOAD_FOLDER.mkdir(exist_ok=True)
      image.save(UPLOAD_FOLDER / image_name)
      no.image = '/static/images/'+ image_name
      db.session.add(no)
      db.session.commit()
      return redirect(f'/movie/{no.id}')

   return render_template('add_movie.html',form=form)
