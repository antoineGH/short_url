from flask_wtf import FlaskForm
from wtforms.fields.html5 import  URLField
from wtforms.validators import DataRequired, ValidationError, URL
from short_url.models import Links

class URLForm(FlaskForm):
    url = URLField('URL', validators=[DataRequired(message="Please enter URL"), URL(message="Please enter Valid URL.")], render_kw={"placeholder": "Shorten your link"})

class URLRetrieveForm(FlaskForm):
    url = URLField('Short URL', validators=[DataRequired(message="Please enter URL"), URL(message="Please enter Valid URL.")], render_kw={"placeholder": "URL from ShortURL"})

    def validate_url(self, url):
        url = Links.query.filter_by(short_url=url.data).first()
        if not url:
            raise ValidationError('That URL doesn\'t exist. Please choose a different one.')

