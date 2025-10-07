from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, AI Journal Assistant!"

if __name__ == "__main__":
    app.run(debug=True)
