from flask import Flask,render_template# Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask Class called 'app'

@app.route('/') # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html",phrase='Pray',times=3)
# def hello_world():
#     return 'Hello World!' # Return the string 'Hellow World!' as a response 

@app.route('/play')
def play():
    return render_template("index00.html")

@app.route('/play/<int:num>')
def playtoo(x):
    return render_template("index00.html",num=num)


@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html",banana=banana,num=num)

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return 'username: ' + username + " , id: " + id


@app.route('/dojo')
def dojo():
    return dojo

@app.route('/say/<string:create>')
def say(create):
    return f"Hi {create}!"

@app.route('/repeat/<int:time>/<string:peat>')
def repeat(time,peat):
    return f"{time*peat}"

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


@app.route('/users')
def user_list():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('users.html',users=users)


@app.errorhandler(404)
def Nf(e):
    return f'"Sorry! No response. Try again'
if __name__=="__main__": # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # run the app in debug mode.s