from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import InputRequired
from ..models import Post,Comment

class PostForm(FlaskForm):
    pitchtitle = TextAreaField('Pitch Title', validators=[InputRequired()])
    pitchdescription = TextAreaField('Pitch Description', validators=[InputRequired()])
    pitchcategory = SelectField('Pitch Category', choices = [('Marketing', 'Business'),('Agriculture','Life'),('Any other')], validators=[InputRequired()])
    # pitchauthor = SelectField('Pitch Author',validators=[InputRequired()])
    submit = SubmitField('Submit Pitch')

class CommentForm(FlaskForm):
    commentdescription = TextAreaField('Pitch Description', validators=[InputRequired()])
    submit = SubmitField('Submit Comment')