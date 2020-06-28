from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL, NumberRange


class UrlForm(FlaskForm):
    url = StringField(
        "url",
        validators=[
            DataRequired(message="Must enter an URL"),
            URL(message="That doesn't look like a valid URL"),
        ],
    )
    lifetime = IntegerField(
        "lifetime [days]",
        default=1,
        validators=[
            DataRequired(message="Must enter URL lifetime"),
            NumberRange(
                min=1, max=31, message="URL lifetime must be between 1 and 31 days"
            ),
        ],
    )
    submit = SubmitField("shorten")
