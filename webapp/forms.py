from flask_wtf import FlaskForm
from requests.sessions import default_headers
from wtforms import BooleanField, StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_name = StringField('Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})
    