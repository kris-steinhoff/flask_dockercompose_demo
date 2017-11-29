from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY=os.getenv('FLASK_SECRET_KEY', 'development key')
))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(1000))
    submitted_at = db.Column(db.DateTime)

    def __init__(self, title, body=None, submitted_at=None):
        self.title = title
        self.body = body

        if submitted_at is None:
            submitted_at = datetime.now()
        self.submitted_at = submitted_at

    def __repr__(self):
        return '<Message %d:%r>' % (self.id, self.title)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print('Initialized the database.')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = Message(request.form['message_title'],
                          request.form['message_body'])
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('home'))

    messages = Message.query.all()
    return render_template('home.html.j2', messages=messages)
