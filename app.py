from flask import Flask, render_template, request, session, redirect
from db_functions import db_connect, db_insert_user, db_find_all, db_delete_one
from db_functions import MONGO_URI

perfiles = db_connect(MONGO_URI, "LinceHack", "Usuarios")

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/perfiles/<string:name>')
def perfil(name='nothing'):
	nombre={
		'user':name
	}
	pe = db_find_all(perfiles, nombre)

	try:
		for p in pe:
			user = p
		print(user)

	finally:
		print("finally")
		return render_template('Perfil.html', name=user)




if __name__ == '__main__':
	app.run(debug=True, port=5000)