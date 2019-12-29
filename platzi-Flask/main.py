from flask import Flask, request, make_response, redirect
# Importamos la clase Flask que no va a permitir generar nuevas instancias de 
# Flask. 
# flask es la extensión específica.

# Creamos nueva instancia de Flask. Le pasamos como parámetro el nombre de la
# aplicación, en este caso el main.py

app = Flask(__name__) 

# Una vez creada nuestra aplicación, crearemos la primera ruta en que se 
# desplegará nuestro primer "hello, world".
## make_response es una variable de flask que, junto con redirect, hará
## la redirección a Hello
## Guardaremos el redirect en una variable para poner una cookie que será igual
## a la ip del usuario. La cookie se llamará "user_ip" y el valor que recibirá
## será el de usr_ip.
## Para que ello funcione tenemos que regresar la respuesta de flask, 
## en la variable response
@app.route('/')
def index():
    usr_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', usr_ip)

    return response

# Para ello crearemos una función que regresará el mensaje Hello, World.
# Debemos ligar con la aplicación para que flask sepa a qué ruta debe ir 
## Cambiamos la ruta para desplegar el mensaje de Hello
@app.route('/hello')
# Usamos un decorador de python, con una función de app, que se llama 
# route, que recibe como parámetro la ruta en que queremos que se corra la 
# función.
# Es decir, cuando el buscador haga una petición a nuestro servidor, va a 
# llegar a la raíz par aregresar el mensahe de la función hello.
## Debemos modificar nuestra ruta hello para que obtenga la ip del usuario desde las
## cookies del browser y no directamente del request
def hello():
    usr_ip = request.cookies.get('user_ip')
    return "Hello, World Flask, Your Ip is {}".format(usr_ip)
