from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class UrlForm(FlaskForm):
    url = StringField("url", validators=[DataRequired(), URL()])
    submit = SubmitField("shorten")
