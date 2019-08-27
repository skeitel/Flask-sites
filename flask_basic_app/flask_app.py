from flask import Flask, render_template
''' If you go to \profile and include a name such as /profile/testname
the webpage will show the text present on the webpage plus "testname"
'''
app = Flask(__name__)

@app.route('/profile/<name>')
def index(name):
    return render_template('profile.html', name = name)


@app.route('/shopping')
#Shows a list of items on the page
def shopping():
    food = ['Cheese', 'Tuna', 'Beef', 'Avocado']
    return render_template('shopping.html', food = food)

if __name__ == '__main__':
    app.run()


# @app.route('/')
# def index():
#     return 'This is the homepage'
#
# #return word based on subdirectory
# @app.route('/tuna')
# def tuna():
#     return 'Tuna is good'
#
# #return username
# @app.route('/profile/<username>')
# def profile(username):
#     return f'<h1>Hello {username}</h1>'
#
#
# #add post number from url to html
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'<h1>Post ID is {post_id}</h1>'
#
# if __name__ == '__main__':
#     app.run(debug = True)