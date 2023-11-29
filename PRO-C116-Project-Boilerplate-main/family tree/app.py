# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Ayansh" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    #Create a variable
    name = 'Ashish'
    # Pass the variable in the template
    return render_template('father.html', father_name = name)
app.run(debug=True)

# define the route to mother webpage
@app.route("/mother")
def mother():
    #Create a variable
    name = 'Nishi'
    # Pass the variable in the template
    return render_template('mother.html', mother_name = name)
app.run(debug=True)


# define the route to friends webpage
@app.route("/friends")
def friends():
    #Create a variable
    name = 'LOL'
    # Pass the variable in the template
    return render_template('friends.html', friends_name = name)
app.run(debug=True)
# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
