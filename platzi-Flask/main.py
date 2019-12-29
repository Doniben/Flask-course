from flask import Flask, request
# Importamos la clase Flask que no va a permitir generar nuevas instancias de 
# Flask. 
# flask es la extensión específica.

# Creamos nueva instancia de Flask. Le pasamos como parámetro el nombre de la
# aplicación, en este caso el main.py

app = Flask(__name__) 

# Una vez creada nuestra aplicación, crearemos la primera ruta en que se 
# desplegará nuestro primer "hello, world".

# Para ello crearemos una función que regresará el mensaje Hello, World.
# Debemos ligar con la aplicación para que flask sepa a qué ruta debe ir 

@app.route('/')
# Usamos un decorador de python, con una función de app, que se llama 
# route, que recibe como parámetro la ruta en que queremos que se corra la 
# función.
# Es decir, cuando el buscador haga una petición a nuestro servidor, va a 
# llegar a la raíz par aregresar el mensahe de la función hello.
def hello():
    usr_ip = request.remote_addr
    return "Hello, World Flask, Your Ip is {}".format(usr_ip)
