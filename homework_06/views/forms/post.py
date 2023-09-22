from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(
        label="title:",
        validators=[
            DataRequired(),
            Length(min=3),
        ]
    )
    body = StringField(
        label="body:",
        validators=[
            DataRequired(),
        ],
    )
    submit = SubmitField(
        label="Submit",
    )
