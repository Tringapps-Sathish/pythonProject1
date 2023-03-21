from flask import Flask

app = Flask(__name__)  # creating the Flask class object
print(__name__)


@app.route('https://python-project1-theta.vercel.app/hello/<name>')
def home(name):
    return f"hello, this is our first flask website {name}"


def about():
    return "This is about page"


app.add_url_rule("https://python-project1-theta.vercel.app/about", "about", about)

if __name__ == '__main__':
    app.run(debug=True)
