import sqlite3
import re
import os
from flask import Flask, request, session, jsonify, redirect, render_template, flash, get_flashed_messages
from flask_session import Session
from datetime import timedelta
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)
app.static_folder = 'static'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure database
DATABASE = 'users.db'

app.secret_key = 'bnjvcwsiurgSDGSfdshgsadGGhbnrw0912835880'

def connect_db():
    db_connection = sqlite3.connect(DATABASE)
    db_connection.row_factory = sqlite3.Row
    return db_connection

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
            completed BOOLEAN,
            notes TEXT,
            exercise TEXT,
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

        remember_me = request.form.get('remember_me')

        if remember_me:
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=7)

        if not username or not password:
            return "Username and password are required.", 400
        
        db = connect_db()
        cursor = db.cursor()

        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[3], password):
            # User is authenticated
            session["user_id"] = user[0]
            session["username"] = user[1]
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

        if confirmation != password:
            flash("Passwords need to be the same!")
            return redirect("/register")

        if not username or not email or not password or password != confirmation:
            flash("Username, email and password are required.")
            return redirect("/register")
        
        # Check if email format is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email!")
    
        db = connect_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email)) 
        existing_user = cursor.fetchone()
        if existing_user:
            flash("Username or email is already in use!")
            return redirect("/register")

        # Hash the password before storing it
        password_hash = generate_password_hash(password)

        # Insert the new user into the users table
        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", (username, email, password_hash))

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
        completed = True if request.form.get("completed") == "on" else False

        db = connect_db()
        cursor = db.cursor()

        if workout_type == "running":
            distance = request.form.get("distance")
            time = request.form.get("time")
            completed = request.form.get("completed")
            notes = request.form.get("notes")
            cursor.execute("INSERT INTO workouts (user_id, workout_type, completed, distance, date, time, notes)VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (user_id, workout_type, completed, distance, date, time, notes))
            
        elif workout_type == "fitness":
            exercise = request.form.get("exercise")
            sets = request.form.get("sets")
            reps = request.form.get("reps")
            time = request.form.get("time")
            completed = request.form.get("completed")
            notes = request.form.get("notes")
            cursor.execute("INSERT INTO workouts (user_id, workout_type, completed, sets, reps, date, time, notes, exercise)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (user_id, workout_type, completed, sets, reps, date, time, notes, exercise))
        
        elif workout_type == "swimming":
            distance = request.form.get("distance")
            time = request.form.get("time")
            completed = request.form.get("completed")
            notes = request.form.get("notes")
            cursor.execute("INSERT INTO workouts (user_id, workout_type, completed, distance, date, time, notes)VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (user_id, workout_type, completed, distance, date, time, notes))


        db.commit()
        db.close()

        flash("Workout succesfully added!")
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
        user_id = session["user_id"]

        db = connect_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM workouts WHERE user_id = ? ORDER BY date DESC", (user_id,))
        workouts = cursor.fetchall()

        db.close()

        return render_template('workouts.html', workouts=workouts)
    else:
        return redirect('/login')
    
# Edit existing workouts on workouts page
@app.route('/edit_workout/<int:workout_id>', methods=["GET", "POST"])
def edit_workout(workout_id):
    if 'user_id' in session:
        if request.method == "POST":
            date = request.form.get("date")
            distance = request.form.get("distance")
            time = request.form.get("time")
            completed = request.form.get("completed")
            notes = request.form.get("notes")
            exercise = request.form.get("exercise")
            sets = request.form.get("sets")
            reps = request.form.get("reps")

            db = connect_db()
            cursor = db.cursor()

            cursor.execute("UPDATE workouts SET date = ?, distance = ?, time = ?, completed = ?, notes = ?, exercise = ?, sets = ?, reps = ? WHERE id = ?",
                           (date, distance, time, completed, notes, exercise, sets, reps, workout_id))

            db.commit()
            db.close()

            flash("Workout updated successfully!")
            return redirect('/workouts')
        else:
            db = connect_db()
            cursor = db.cursor()

            cursor.execute("SELECT * FROM workouts WHERE id = ?", (workout_id,))
            workout = cursor.fetchone()

            db.close()

            return render_template('edit_workout.html', workout=workout)
    else:
        return redirect('/login')

# Delete existing workout
@app.route('/delete_workout/<int:workout_id>', methods=["GET", "POST"])
def delete_workout(workout_id):
    if 'user_id' in session:
        db = connect_db()
        cursor = db.cursor()

        cursor.execute("DELETE FROM workouts WHERE id = ?", (workout_id,))
        db.commit()
        db.close()

        flash("Workout deleted successfully!")
        return redirect('/workouts')
    else:
        return redirect('/login')


@app.route('/form_running')
def form_running():
   if 'user_id' in session:
       return render_template('form_running.html')
   else:
       return redirect('/login')


@app.route('/form_fitness')
def form_fitness():
   if 'user_id' in session:
       return render_template('form_fitness.html')
   else:
       return redirect('/login')


@app.route('/form_swimming')
def form_swimming():
   if 'user_id' in session:
       return render_template('form_swimming.html')
   else:
       return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been succesfully logged out!")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
