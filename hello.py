from flask import Flask
import random

app = Flask(__name__)
### allows for real time changes to debug instead of deactiavting
### and activate service again.
app.config["DEBUG"] = True


### / represents home page path to a specific function.
### its a decorator that runs the code in the specific url
@app.route("/")
@app.route("/hello")
def hello():
    page = """
    <h1>Here's a random number: {0}</h1>
    <form>
       <button>New Number</button>
    </form>
    """
    num = random.randint(1, 25)
    return page.format(num)


### we can control a multi-page website by adding different functions and
## routes to the python program.
@app.route("/goodbye")
def goodbye():
    message = "<h2>This is the second page!</h2>"
    return message


@app.route("/third_page")
def third_page():
    message = "<h2> This is my third page</h2>"
    return message


if __name__ == "__main__":
    ### app.run creates a loop, flask server waits for the request to come in. ONce it  receives it responds and waits again
    ### this repeats until we terminate flask.
    app.run()
