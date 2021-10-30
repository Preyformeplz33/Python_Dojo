from flask import Flask# Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask Class called 'app'

@app.route('/') # The "@" decorator associates this route with the function immediately following

def hello_world():
    return 'Hello World!' # Return the string 'Hellow World!' as a response 

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return f"Hello {banana * num}"

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

if __name__=="__main__": # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # run the app in debug mode.