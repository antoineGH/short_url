from flask import Blueprint, render_template
from short_url.urls.utils import encode, decode

urls = Blueprint('urls', __name__)

@urls.route('/')
@urls.route('/home')
def home():
    return render_template('home.html', title='Get ShortURL')

@urls.route('/retrieve')
def retrieve():
    return render_template('retrieve.html', title='Retrieve URL')
