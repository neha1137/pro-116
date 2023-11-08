# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "neha" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/flask_2")
def father():

    name = "dad"
    age = "50"

    return render_template('index.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/flask_3")
def mother():

    name = "mom"
    age = "40"

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/flask_4")
def friends():

    name = "friend"
    age ="20"

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
