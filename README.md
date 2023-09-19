# WRKOUT  
Video demo: https://www.youtube.com/watch?v=xDhdh4TgEvw

# Description

WRKOUT is a web app that is tailored towards fitness, running or swimming enthousiasts who would like to log their workouts.
It is supposed to be a very basic clone of other major fitness apps like Garmin or Strava, but purely as a web app instead of mobile.

This project is built upon a full stack consisting of Python and Flask for the backend, SQLite3 for the database aswell as HTML, CSS and basic JS for the frontend.

# Table of Contents
  - 1.1  Homepage & About
  - 2.1  Register
  - 2.2  Login
  - 3.1  Dashboard
  - 3.2  Add Workouts
  - 3.3  My Workouts
  - 3.4  Logout

# 1.1 - Homepage
The landing page for the website, provides details about what kind of site this is and who the targeted audience is.


![wrkout1](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/af06d48e-a400-4092-a697-071b8274ed48)


![Recording 2023-09-19 at 19 56 43](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/fc99cfad-8fa7-41a5-8189-56deca25a69a)



# 2.1 - Register
Register form where users need to input a unique email and username and must have matching passwords.


![register2](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/5fbd7c2f-28ee-4f63-9c2a-1672976efaa9)


![register1](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/70942b72-bded-49e6-ae6f-722c0754d481)


![Recording 2023-09-19 at 19 40 20](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/2736688f-edfb-4824-bff9-3a9563d3add3)



# 2.2 - Login
Users have to input the same input credentials as they have provided in the register screen. Includes a function to remember the user information for 7 days by checking the box, after 7 days the user's session will pop automatically.


![login1](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/bbd5a70d-46a6-4d5b-9073-829d7afae6f3)


![Recording 2023-09-19 at 19 41 41](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/f2708ad1-f65c-4cef-964c-5bc13de979d1)


# 3.1 - Dashboard
User's homepage where they can add new workouts, right now there's 3 types of workouts to choose from namely: Running, Fitness and Swimming.


![homescreen](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/da8cf838-1044-4297-a15b-377036aa3fa2)


# 3.2 - Add Workouts
Displayed here we see the add fitness form. Once filled in the user can decide whether he has already completed the workout, or if he's planning to do the workout in the future by either checking or unchecking the button.


![add-workout](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/df99a00b-6321-4a78-a5a7-df869321ac70)


![Recording 2023-09-19 at 20 14 03](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/646ff507-c856-493d-8f9d-d7dfe7b79b1a)


# 3-3 - My Workouts
Once the workout has been added the user can either edit or delete his workouts here by simpling hovering over the intended workout and clicking either of the two buttons. 
If the workout is listed as red, the workout is either not completed or planned for the future. If the workout is listed as green then the user has checked it off as completed.


![Recording 2023-09-19 at 20 17 50](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/76c632d8-1d8e-4b78-8a22-b6c0fcecb563)


![Recording 2023-09-19 at 19 33 38](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/b7893cdf-4f7c-420d-b0cc-dd52f5495704)


# 3.4 - Logout
To logout simply click the logout button and the session will pop and you will have to sign in again to enter the website.


![Recording 2023-09-19 at 20 20 56](https://github.com/MaxK9999/Final-project-CS50X/assets/129183382/206b9456-c16f-4799-95c1-9318f2d9460a)


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
