from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_headlines, get_category, article_source
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    source = get_source()
    headlines = get_headlines()
    return render_template('index.html',sources =source, headlines = headlines)
@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles = article_source(id)
    return render_template('article.html',articles= articles, id =id)


@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)

