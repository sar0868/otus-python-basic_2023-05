from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
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
        ]
    )
    # email = StringField(
    #     label="email:",
    #     validators=[
    #         Email(),
    #     ]
    # )
    submit = SubmitField(
        label="Submit",
    )
