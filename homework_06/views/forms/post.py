from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email, Length


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
    user_id = StringField(
        label="user_id:",
        validators=[
            DataRequired(),]
    )
    submit = SubmitField(
        label="Submit",
    )
