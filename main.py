from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/2b771bfc6659fc72cc85"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("index.html", data=data)

@app.route('/blog/<int:num>')
def post(num):
    blog = "https://api.npoint.io/2b771bfc6659fc72cc85"
    response1 = requests.get(blog)
    all_data = response1.json()
    return render_template("post.html", data=all_data, index=num)

if __name__ == "__main__":
    app.run(debug=True)
