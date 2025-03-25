from flask import Flask, render_template, request, redirect, url_for
from models import Post

app = Flask(__name__)

@app.route('/')
def index():
    posts = Post.get_all()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title, content)
        post.save()
        return redirect(url_for('index'))
    return render_template('create_post.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.get_by_id(post_id)
    return render_template('post.html', post=post)

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.get_by_id(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        Post.update(post_id, title, content)
        return redirect(url_for('view_post', post_id=post_id))
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    Post.delete(post_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    Post.create_table()
    app.run(debug=True)