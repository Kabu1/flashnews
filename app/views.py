from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)
@app.route('/article/<id>')
def movie(article_id):

    '''
    View article page function that returns the movie details page and its data
    '''
    return render_template('article.html',articles = articles, id=id)



