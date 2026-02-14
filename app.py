from flask import Flask, render_template, request, session, redirect, url_for
import psycopg
app = Flask(__name__)
app.secret_key = b'5$goongoonsahur\n\cex]/'
usuarios = []

DB_URL = "postgresql://neondb_owner:npg_qGXk2mYF7ZyA@ep-delicate-pond-ab2yyzk8-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
conn = psycopg.connect(DB_URL)

pages =['home', 'login', 'register', 'play']

@app.route('/')
@app.route('/home')
def home():

    if 'username' in session:
        username = session['username']
        return render_template("index.html", username=username, pages=pages)
    else:
        return render_template("index.html",  pages=pages)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for usuario in usuarios:
            if usuario[0] == username and usuario[1] == password:
                session['username'] = username
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

        crs = conn.cursor()
        crs.execute("INSERT INTO msg (username, txt) VALUES (%s, %s)", (username, password))
        conn.commit()

        msg ="Goon adiciogoon"
        return render_template("register.html", msg= msg )

    else:
        return render_template("register.html")



@app.route('/play')
def play():
    return render_template("play.html", pages=pages)



@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))

app.run(debug=True, host='0.0.0.0')