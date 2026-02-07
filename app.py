from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = []


pages =['home', 'login', 'register', 'play']

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", pages=pages)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for usuario in usuarios:
            if usuario[0] == username and usuario[1] == password:
                return render_template("index.html", pages=pages)

        msg = " Goon não goontrado!"
        return render_template("login.html",msg=msg)

    else:
        return render_template("login.html")

@app.route('/register', methods =['GET','POST'])
def register():
    global usuarios

    if request.method =='POST':

        username = request.form['username']
        password = request.form['password']

        print(username,password)

        for usuario in usuarios:
            if usuario[0] == username:
                #return render_template("register.html", pages=pages)
                msg = "Goon já"
                return "Usuario existente"

        usuarios.append((username,password))
        msg ="Goon adiciogoon"
        return render_template("register.html", msg= msg )

    else:
        return render_template("register.html")



@app.route('/play')
def play():
    return render_template("play.html", pages=pages)

app.run(debug=True, host='0.0.0.0')

