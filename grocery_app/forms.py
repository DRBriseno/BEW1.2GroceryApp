from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from grocery_app.models import GroceryStore, GroceryItem, ItemCategory, User

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=30)])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=['PRODUCE', 'DELI', 'BAKERY', 'PANTRY', 'FROZEN', 'OTHER'], validators=[DataRequired()])
    photo_url = StringField('Photo Url', validators=[DataRequired()])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False, get_label='title')
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign-Up')

    def validateUsername(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken.')



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log-In')


