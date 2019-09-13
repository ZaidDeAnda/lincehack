from flask import Flask, render_template, request, session, redirect
from db_functions import db_connect, db_insert_user, db_find_all, db_delete_one
from db_functions import MONGO_URI
from forms import CreationForm

perfiles_usuario = db_connect(MONGO_URI, "LinceHack", "Usuarios")
perfiles_organizacion = db_connect(MONGO_URI, "LinceHack", "Organizaciones")

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/userprofiles/<string:name>')
def perfil_user(name='nothing'):
	nombre={
		'user':name
	}
	pe = db_find_all(perfiles_usuario, nombre)

	try:
		for p in pe:
			user = p
		print(user)

	finally:
		print("finally")
		return render_template('Perfil.html', name=user)

@app.route('/orgprofiles/<string:name>')
def perfil_org(name='nothing'):
	nombre={
		'user':name
	}
	pe = db_find_all(perfiles_organizacion, nombre)

	try:
		for p in pe:
			user = p
		print(user)

	finally:
		print("finally")
		return render_template('Perfil.html', name=user)

@app.route('/creation/org', methods=['GET','POST'])
def creation_org():
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