#from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

# Index
@app.route('/')
def home():
    return render_template('home.html')
    #return '<h1> Hello Flask </h1>'
    #return 'Hello Flask'

#About
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)
#    app.run()


