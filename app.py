from flask import Flask, render_template, request, session, redirect
from db_functions import db_connect, db_insert_user, db_find_all, db_delete_one, db_find_one
from db_functions import MONGO_URI
from forms import CreationForm

perfiles_usuario = db_connect(MONGO_URI, "LinceHack", "Usuarios")
perfiles_organizacion = db_connect(MONGO_URI, "LinceHack", "Organizaciones")
perfiles_becas = db_connect(MONGO_URI, "LinceHack", "Becas")

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
	item = db_find_all(perfiles_organizacion)
	return render_template('index.html', item=item)

@app.route('/userprofiles/<string:name>')
def perfil_user(name='nothing'):
	nombre={
		'user':acronimo
	}
	item = db_find_one(perfiles_usuario, nombre)
	return render_template('olimpiada.html', name=user)

@app.route('/orgprofiles/<string:acronimo>')
def perfil_org(acronimo='nothing'):
	nombre={
		'Acrónimo':acronimo
	}
	item = db_find_one(perfiles_organizacion, nombre)
	return render_template('olimpiada.html', item=item)

@app.route('/creation/org', methods=['GET','POST'])
def creation_org():
	form = CreationForm(request.form)
	if request.method == 'POST':
		Nombre = form.Nombre.data
		Acrónimo = form.Acrónimo.data
		Photo = form.Photo.data
		Descripción = form.Descripción.data
		Tags = form.Tags.data
		Tags = Tags.split(",")
		Frase = form.Frase.data
		Foto_aux = form.Foto_aux.data
		Titulo_noticia = form.Titulo_noticia.data
		Cuerpo_noticia = form.Cuerpo_noticia.data
		Convocatoria = form.Convocatoria.data
		Redes_Sociales = form.Redes_Sociales.data
		if Nombre != None and Photo != None and Descripción != None and Tags != None and Acrónimo != None and Frase != None and Foto_aux != None and Titulo_noticia != None and Cuerpo_noticia != None and Convocatoria != None and Redes_Sociales != None:
			Org = {
				'Nombre': Nombre,
				'Acrónimo': Acrónimo,
				'photo': Photo,
				'Descripción': Descripción,
				'Tags': Tags,
				'Frase': Frase,
				'Foto_aux': Foto_aux,
				'Titulo_noticia': Titulo_noticia,
				'Cuerpo_noticia': Cuerpo_noticia,
				'Convocatoria': Convocatoria,
				'Redes_Sociales': Redes_Sociales
			}
			db_insert_user(perfiles_organizacion, Org)
			return redirect('/')
	return render_template('Register.html')

@app.route('/creation/user', methods=['GET','POST'])
def creation_user():
	form = CreationForm(request.form)
	if request.method == 'POST':
		Nombre = form.Nombre.data
		Photo = form.Photo.data
		Descripción = form.Descripción.data
		Tags = form.Tags.data
		if Nombre != None and Photo != None and Descripción != None and Tags != None:
			Org = {
				'user': Nombre,
				'photo': Photo,
				'Descripción': Descripción,
				'Tags': Tags
			}
			db_insert_user(perfiles_usuario, Org)
			return redirect('/')
	return render_template('Register.html')
if __name__ == '__main__':
	app.run(debug=True, port=5000)