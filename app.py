from flask import Flask

app = Flask(__name__)

# @app.route() determines what route the view will be at
# in this case it will be going to the index (or home)

# the actual view here 'def index()' is a very simple one line response which will return 'Hello World!' to the browser


@app.route('/')
def index():
    return 'Hello World!'

# this method is where you will run the server that is provided by Flask.
# all this is doing is checking this app has the name of __main__ and then running the server.
if __name__ == '__main__':
    app.run()
