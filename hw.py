# Everything is running; now to get the HTML to display 10-19-15aw
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('jinja_temp.html', my_string="Hello You are Here!",
                           my_list=[0,1,2,3,4,5])

@app.route("/home")
def home():
    return render_template('jinja_temp.html',
                           my_string="I'm the home page",
                           my_list=[0,1,2,3,4,5])

@app.route("/about")
def about():
    return render_template('jinja_temp.html',
                            my_string="I'm the about page",
                            my_list=[0,1,2,3,4,5])

@app.route("/contact")
def contact():
    return render_template('jinja_temp.html',
                           my_string="I'm the contact page",
                           my_list=[0,1,2,3,4,5])
                       
                           
@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())                           
                           
@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname,lastname):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(lastname[0:3].title()+firstname[0:2].title())
    
                           
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)