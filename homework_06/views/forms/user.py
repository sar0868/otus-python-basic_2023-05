from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    name = StringField(
        label="name:",
        validators=[
            DataRequired(),
            Length(min=3),
        ]
    )
    username = StringField(
        label="username:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    email = EmailField(
        label="email:",
        validators=[
            Email(),
        ]
    )
    submit = SubmitField(
        label="Submit",
    )
