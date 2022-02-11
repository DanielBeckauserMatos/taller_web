from flask import Flask, escape, request, render_template, url_for  # Importar la libreria



app = Flask(__name__)   # Inicializamos la app con el nombre

@app.route('/')     #  Definimos que ne la ruta de inicio será aplicada la funcion hola
def hola():
    return 'Hi Penguins!'   # Retorna Hi Penguins!

@app.route('/coach')
def hola_coaches():
    nombre = 'Dani'
    devolver = request.args.get('nombre', nombre)
    return f'Hola, soy {escape(devolver)}'
    
@app.route('/inicio')   # Creamos la ruta inicio
def inicio():
    return render_template('inicio.html')

@app.route('/contacto') # Creamos la ruta contacto
def contacto():
    return render_template('contacto.html')



app.run(debug=True)     # Para ejecutar 

