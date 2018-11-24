from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required, DataRequired, Email


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Blog title',validators=[DataRequired()])
    post = TextAreaField('Write your blog',validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Write your comment',validators=[DataRequired()])
    submit = SubmitField('Submit')


class SubscribeForm(FlaskForm):
    username = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    submit = SubmitField('Submit')