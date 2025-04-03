from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    # debug=True means it automatically reloads on file changes
    app.run(debug=True)