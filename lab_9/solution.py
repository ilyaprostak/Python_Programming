from flask import Flask, rendertemplate, request
from flasksqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primarykey=True)
    text = db.Column(db.String(255), nullable=False)
    important = db.Column(db.Boolean, default=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        important = True if request.form.get('important') else False
        note = Note(text=text, important=important)
        db.session.add(note)
        db.session.commit()
    notes = Note.query.all()
    return rendertemplate('index.html', notes=notes)


@app.route('/clear')
def clear():
    Note.query.delete()
    db.session.commit()
    return 'Notes cleared'


if __name__ == 'main':
    app.run(debug=True)