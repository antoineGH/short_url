from datetime import datetime
from flask import Blueprint, render_template, redirect
from short_url.urls.utils import encode, decode
from short_url.models import Links
from short_url.urls.forms import URLForm, URLRetrieveForm
from short_url import db

urls = Blueprint('urls', __name__)

@urls.route('/')
@urls.route('/home', methods=['GET', 'POST'])
def home():
    form = URLForm()
    url = None
    if form.validate_on_submit():
        link = Links(url=form.url.data.lower())
        db.session.add(link)
        db.session.commit()
        short_url = encode(link.id)
        link.short_url = 'http://127.0.0.1:5000/' + short_url
        db.session.add(link)
        db.session.commit()
        url = link.short_url
    return render_template('home.html', title='Get ShortURL', form=form, url=url)

@urls.route('/retrieve', methods=['GET', 'POST'])
def retrieve():
    form = URLRetrieveForm()
    url = None
    if form.validate_on_submit():
        link = Links.query.filter_by(short_url=form.url.data).first()
        url = link.url
        date_created = datetime.strftime(link.date_created, '%d %B %Y')
    return render_template('retrieve.html', title='Retrieve URL', form=form, url=url, link=link, date_created=date_created)

@urls.route('/<string:url>')
def redirect_url(url):
    url_id = decode(url)
    url_decoded = Links.query.get_or_404(url_id)
    url_decoded.accessed += 1
    url_decoded.last_accessed = datetime.utcnow()
    db.session.commit()
    return redirect(url_decoded.url)
