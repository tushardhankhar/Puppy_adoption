import os
from flask import Flask , render_template , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from form import Add_form , Delete_form

app = Flask(__name__,template_folder='template')

app.config['SECRET_KEY'] = 'asfg'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class puppies(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
         return f"Puppy name {self.name}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add():

    ad = Add_form()

    if ad.validate_on_submit():

        name = ad.breed.data

        new_pup = puppies(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list'))
    
    return render_template('add.html',ad=ad)


@app.route('/list')
def list():

    puppy = puppies.query.all()
    return render_template('list.html',puppy=puppy)


@app.route('/delete',methods=['GET','POST'])
def delete():

    dl = Delete_form()

    if dl.validate_on_submit():

        pop_puppy = dl.id.data
        popp = puppies.query.get(pop_puppy)

        db.session.delete(popp)
        db.session.commit()

        return redirect(url_for('list'))
    return render_template('delete.html',dl=dl)

if __name__ == '__main__':
    app.run(debug=True)