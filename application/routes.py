from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts
from application.forms import PostForm

@app.route('/')
@app.route('/main_lib')
def main_lib():
	return render_template('main_lib.html', title='My Library')

@app.route('/login')
def login():
	return render_template('login.html', title='login')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')

	@app.route('/manage_lib', methods=['GET', 'POST'])
def manage_lib():
    form = BookForm()
    if form.validate_on_submit():
        bookData = Books(
            first_name = form.first_name.data,
            surname = form.last_name.data,
            title = form.title.data,
            content = form.content.data,
			pages = form..data,
			language = form.language.data,
			comment = form.comment.data,
			date_read = form.date_read.data
        )

        db.session.add(bookData)
        db.session.commit()

        return redirect(url_for('main_lib'))

    else:
        print(form.errors)

    return render_template('manage_lib.html', title='Manage my Entries', form=form)