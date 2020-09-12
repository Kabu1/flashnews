from flask import render_template
from app import app
from .request import get_source,get_headlines, get_category, article_source
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    source = get_source()
    headlines = get_headlines()
    return render_template('index.html',sources =source, headlines = headlines)
@app.route('/article/<int:id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles = article_source(id)
    return render_template('article.html',articles= articles, id =id)




