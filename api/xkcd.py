from flask import Flask
app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def say_hello():
    print("Hello, there\n")
say_hello()

if __name__ == "__main__":
    app.run(debug=True)
