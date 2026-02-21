from flask import Flask, render_template, request, session, redirect, url_for
import psycopg
app = Flask(__name__)
app.secret_key = b'5$goongoonsahurncex]/'
usuarios = []

DB_URL = "postgresql://neondb_owner:npg_skLYJ5R9hIKe@ep-billowing-voice-abofarmr-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
conn = psycopg.connect(DB_URL)

pages =['home', 'login', 'register', 'play']

@app.route('/')
@app.route('/home')
def home():

    if 'username' in session:
        username = session['username']
        return render_template("index.html", username=username, pages=pages)
    else:
        return render_template("index.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']




        crs = conn.cursor()
        crs.execute('SELECT * FROM "Users" WHERE "Name" = %s AND "Password" = %s', (username, password))
        user = crs.fetchone()

        if user:
             session ["username"] = user [1]
             return render_template("index.html")
        else:
            msg ="Goonsário ou goonword ingoonretos"
            return render_template("login.html",msg = msg)


    else:
        return render_template("login.html")



@app.route('/register', methods =['GET','POST'])
def register():
    global usuarios

    if request.method =='POST':

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        print(username,password)

        crs = conn.cursor()
        crs.execute('SELECT 1 FROM "Users" WHERE "Name" = %s', (username,))
        user = crs.fetchone()

        if user:
            msg=" Goon já goonxiste"
            return render_template("register.html", msg= msg)


        crs = conn.cursor()
        crs.execute('INSERT INTO "Users" ("Name", "Email", "Password") VALUES (%s, %s, %s)', (username, email, password))
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