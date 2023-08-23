import sqlite3
import os
from flask import Flask, request, session, jsonify, redirect, render_template, flash, get_flashed_messages
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)
app.static_folder = 'static'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure database
DATABASE = 'users.db'

app.secret_key = 'bnjvcwsiurghbnrw0912835880'

def connect_db():
    return sqlite3.connect(DATABASE)

def create_users_table():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )              
    ''')

def create_workouts_table():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            workout_type TEXT NOT NULL,
            distance REAL,
            time INTEGER,
            sets INTEGER,
            reps INTEGER,
            date DATE NOT NULL,
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    db.commit()
    db.close()

# Call create_users_table and workouts_table
create_users_table()
create_workouts_table()


# login prompt 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Username and password are required.", 400
        
        db = connect_db()
        cursor = db.cursor()

        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            # User is authenticated
            session["user_id"] = user[0]
            return redirect("/dashboard")
        else:
            flash ("Invalid username or password.")
        
    return render_template("login.html") 


# Register route (for creating new users)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not email or not password or password != confirmation:
            return "Username, email and password are required.", 400
    
        db = connect_db()
        cursor = db.cursor()

        # Hash the password before storing it
        password_hash = generate_password_hash(password)

        # Insert the new user into the users table
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))

        db.commit()
        db.close()

        flash("Account created succesfully!")
        return redirect("/dashboard")
    
    else:
        return render_template("register.html")  


# Add workouts on workouts page
@app.route("/add_workout", methods=["POST"])
def add_workout():
    if request.method == "POST":
        workout_type = request.form.get("workout_type")
        date = request.form.get("date")
        user_id = session["user_id"]

        db = connect_db()
        cursor = db.cursor()

        if workout_type == "running":
            distance = request.form.get("distance")
            time = request.form.get("time")
            completed = request.form.get("completed")
            cursor.execute("INSERT INTO workouts (user_id, workout_type, completed, distance, date, time)VALUES (?, ?, ?, ?, ?, ?)",
                            (user_id, workout_type, completed, distance, date, time))
            
        elif workout_type == "fitness":
            sets = request.form.get("sets")
            reps = request.form.get("reps")
            time = request.form.get("time")
            completed = request.form.get("completed")
            cursor.execute("INSERT INTO workouts (user_id, workout_type, completed, sets, reps, date, time)VALUES (?, ?, ?, ?, ?, ?)",
                            (user_id, workout_type, completed, sets, reps, date, time))
        
        elif workout_type == "swimming":
            distance = request.form.get("distance")
            time = request.form.get("time")
            completed = request.form.get("completed")
            cursor.execute("INSERT INTO workouts (user_id, workout_type, completed, distance, date, time)VALUES (?, ?, ?, ?, ?, ?)",
                            (user_id, workout_type, completed, distance, date, time))


        db.commit()
        db.close()

        flash("Running workout succesfully added!")
        return redirect("/workouts")
    
    return render_template("workouts.html")


# Routing for different pages (including 'user_id' only pages)
@app.route('/')
def index():
    user_is_authenticated = False
    return render_template('index.html', user_is_authenticated=user_is_authenticated)

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')
    
@app.route('/workouts')
def workouts():
    if 'user_id' in session:
        return render_template('/workouts.html')
    else:
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been succesfully logged out!")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
