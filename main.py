from flask import Flask, render_template
import requests
URL = 'https://api.npoint.io/c790b4d5cab58020d391'
app = Flask(__name__)

response = requests.get(url=URL)
response.raise_for_status()
data = response.json()



@app.route('/')
def home():
    return render_template('index.html', data=data)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog in data:
        if blog["id"] == index:
            requested_post = blog
            print(requested_post['body'])
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
