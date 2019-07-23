from flask import Flask, render_template, request, redirect, url_for
from sklearn.externals import joblib
import numpy as np
from models import db, User
from forms import UsersForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
db.init_app(app)

app.secret_key = "e14a-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():

    form = UsersForm()
    if request.method == 'GET':
        return render_template('add_user.html', form=form)
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

@app.route('/read-user', methods=['GET'])
def read():
    names = User.query.all()
    return render_template('read.html', names=names)

@app.route('/delete-user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.filter_by(user_id = user_id).first()
    db.session.delete(user)
    db.session.commit()
    print(user.first_name)
    return redirect('/read-user')

if __name__ == '__main__':
  app.debug = True
  app.run()