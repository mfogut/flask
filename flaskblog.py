from flask import Flask , render_template
app = Flask(__name__)

posts = [
    {
    'author': 'Fatih Ogut',
    'title' : 'Blog Post1',
    'content' : 'First Post Content',
    'date_posted' : 'January 08 2020'
    },
    {
    'author': 'Niler Ogut',
    'title' : 'Blog Post2',
    'content' : 'Second Post Content',
    'date_posted' : 'January 09 2020'
    }

]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
