A Minimal Application
A minimal Flask application looks something like this:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
So what did that code do?

First we imported the Flask class. An instance of this class will be our WSGI application.

Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

We then use the route() decorator to tell Flask what URL should trigger our function.

The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

Save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.

To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option.

$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
Application Discovery Behavior
As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app. See Command Line Interface for more details.

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production. For deployment options see Deploying to Production.

Now head over to http://127.0.0.1:5000/, and you should see your hello world greeting.

If another program is already using port 5000, you’ll see OSError: [Errno 98] or OSError: [WinError 10013] when the server tries to start. See Address already in use for how to handle that.

Externally Visible Server
If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

$ flask run --host=0.0.0.0
This tells your operating system to listen on all public IPs.

Command Line Interface
Installing Flask installs the flask script, a Click command line interface, in your virtualenv. Executed from the terminal, this script gives access to built-in, extension, and application-defined commands. The --help option will give more information about any commands and options.

Application Discovery
The flask command is installed by Flask, not your application; it must be told where to find your application in order to use it. The --app option is used to specify how to load the application.

While --app supports a variety of options for specifying your application, most use cases should be simple. Here are the typical values:

(nothing)
The name “app” or “wsgi” is imported (as a “.py” file, or package), automatically detecting an app (app or application) or factory (create_app or make_app).

--app hello
The given name is imported, automatically detecting an app (app or application) or factory (create_app or make_app).