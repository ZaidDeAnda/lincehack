from flask import Flask, render_template, request, session, redirect

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Perfiles/<name>')
def perfil(name='Nada'):
	return render_template('Perfil.html', name=name)

if __name__ == '__main__':
	app.run(debug=True, port=5000)