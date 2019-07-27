from flask import render_template
from app import app
from .request import get_sources

#views
@app.route('/')
@app.route('/watchdogs')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting the news sources
    business_sources=get_sources('business')
    entertainment_sources=get_sources('entertainment')
    general_sources=get_sources('general')
    health_sources=get_sources('health')
    science_sources=get_sources('science')
    sports_sources=get_sources('sports')
    tech_sources=get_sources('technology')

    print(news_sources)

    title = 'WatchDogs News App'
    return render_template('index.html',title=title,source=news_sources)


@app.route("/watchdogs/<source_id>")
def news_source(source_id):
    '''
    View new_source page function that returns a news source page and its data
    '''
    return render_template('newsSource.html',id =source_id)
