from app import app
from app.create_fake_users import fake_users
from flask import render_template, flash, redirect, url_for
from app.models import User
from app.download_users_pdf import download_users_data
from app.encrypted_pdf import encrypt_pdf


def limit_num_fake_users():
    """Create fake users and limit them to 1000."""
    db_users = User.query
    if db_users.count() >= 1000:
        fake_db_users = db_users.limit(1000)
    else:
        fake_users(100)
    return fake_db_users


@app.route('/')
@app.route('/index')
def index():
    """Render the index page."""
    all_users = limit_num_fake_users()
    return render_template('index.html', all_users=all_users)



@app.route('/download-users-pdf')
def download_users():
    """Download a PDF of all users."""
    download_users_data()
    encrypt_pdf(
        input_pdf='app/static/files/users.pdf',
        password='password')
    return redirect(url_for('index'))
