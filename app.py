from flask import Flask, render_template, request

app = Flask(__name__)

pages =['home', 'login', 'register', 'play']

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", pages=pages)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        print(name, password)
        return "Conteudo enviado!"
    else:
        return render_template("login.html", pages=pages)

@app.route('/register', methods =['GET','POST'])
def register():
    if request.method =='POST':
        name = request.form['name']
        password = request.form ['password']

        print(name,password)
        return "Conteudo enviado!"
    else:
        return render_template("register.html", pages=pages)

@app.route('/play')
def play():
    return render_template("play.html", pages=pages)

app.run(debug=True, host='0.0.0.0')

