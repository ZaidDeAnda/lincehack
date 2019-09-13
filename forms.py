from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class CreationForm(Form):
    Nombre = StringField('Nombre', validators=[DataRequired()])
    Photo = StringField('url de la foto', validators=[DataRequired()])
    Descripción = StringField('Breve descripción', validators=[DataRequired()])
    Tags = StringField('Inserte un tag', validators=[DataRequired()])

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
