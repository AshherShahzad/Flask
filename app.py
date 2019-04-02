#from flask import Flask
from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()

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

#Articles
@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

#Single Article
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',article=article)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
#    app.run()


