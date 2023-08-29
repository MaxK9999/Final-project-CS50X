# WRKOUT  

# Description

WRKOUT is a web app that is tailored towards fitness, running or swimming enthousiasts who would like to log their workouts.
It is supposed to be a very basic clone of other major fitness apps like Garmin or Strava, but purely as a web app instead of mobile.

This project is built upon a full stack consisting of Python and Flask for the backend, SQLite3 for the database aswell as HTML, CSS and basic JS for the frontend.


# Source Files

- app.py - Containing all of the necessary Python code to run the backend operation

- users.db - Database that logs all the user data including login information such as username, email and a hashed password. It also logs all the input workouts into a seperate workouts table that is connected to each seperate user via user id.

- static folder - Here you will find all the necessary static files such as CSS, JS and all the pictures used.
  
- templates folder- Consists of all the templates used to render different HTML pages that are linked through Flask extension.
  
- todo.txt - Todo list that highlights my progress for this project and possible future plans.

# Tech Stack

Python - The backend is completely dependent on it aswell as Flask. I've used this language since I've familiriazed myself quite well with it and I'm quite comfortable with it.

Flask - In combination with Python I've decided to use Flask for the authentication and easiness with implementing code to HTML. 

SQLite3 - Since the project is small enough and I'm already accustomed to it through CS50X this was pretty much a no brainer for me to use instead of bigger SQL databases.

HTML/CSS - All hand written with no frameworks, I decided to take on the challenge to write everything myself from scratch for a better learning experience and understanding of frontend overall.


# About Me

My name is Maxim Koltypin, born and raised in The Netherlands in 1999 and currently working as a Marine 1st Class in the Royal Dutch Marine Corps.
I got the inspiration to make this web app when my friends and I were logging our fitness progress through an Excel spreadsheet. After this I decided to make this my final project to see if I was up to the task to make my own program where me and my loved ones could log our fitness (and other sports!) progress.
