from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import BooleanField
from wtforms.validators import DataRequired


class CreationForm(Form):
    Nombre = StringField('Nombre', validators=[DataRequired()])
    Acrónimo = StringField('Acrónimo', validators=[DataRequired()])
    Photo = StringField('url de la foto', validators=[DataRequired()])
    Descripción = StringField('Breve descripción', validators=[DataRequired()])
    Tags = StringField('Inserte un tag', validators=[DataRequired()])
    Frase = StringField('Inserte una frase', validators=[DataRequired()])
    Foto_aux = StringField('url de la foto de la noticia', validators=[DataRequired()])
    Titulo_noticia = StringField('Inserte un título', validators=[DataRequired()])
    Cuerpo_noticia = StringField('Inserte la descripción', validators=[DataRequired()])
    Redes_Sociales = StringField('Inserte el facebook de la org', validators=[DataRequired()])
    Convocatoria = BooleanField('Escoja si la convocatoria está disponible', validators=[DataRequired()])

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
