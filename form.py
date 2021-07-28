from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , IntegerField
from wtforms.validators import DataRequired

class Add_form(FlaskForm):

    breed = StringField('Enter Name of Dog :',validators=[DataRequired()])
    submit = SubmitField('Add Puppy')

class Delete_form(FlaskForm):

    id = IntegerField('Enter the Id number')
    submit = SubmitField('Delete Puppy')