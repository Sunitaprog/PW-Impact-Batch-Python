from flask import Flask
app1=Flask(__name__)

@app1.route("/")
def hello():
    return "<h1>hello_world!!!</h1>"


if __name__ == "__main__":
    app1.run(host="0.0.0.0")