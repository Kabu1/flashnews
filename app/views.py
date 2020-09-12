from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Welcome to Flash News'
    return render_template('index.html',title = title)
@app.route('/article/<int:id>')
def movie(article_id):

    '''
    View article page function that returns the movie details page and its data
    '''
    return render_template('article.html',title = title)



