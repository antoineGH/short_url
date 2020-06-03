from flask import Blueprint, render_template, request

urls = Blueprint('urls', __name__)

@urls.route('/')
@urls.route('/home')
def home():
        return render_template('home.html', title='Home')