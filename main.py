from flask import Flask

app = Flask("Web Application")  # creating the Flask class object
print(__name__)


@app.route('/hello/<name>')
def home(name):
    return f"hello, this is our first flask website {name}"


def about():
    return "This is about page"


app.add_url_rule("/about", "about", about)

if __name__ == '__main__':
    app.run(debug=True)
