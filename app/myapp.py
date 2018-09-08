from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"
 
@app.route("/index")
def index():
    return "Welcome to PySangamam"
if __name__ == "__main__":
    app.run()
