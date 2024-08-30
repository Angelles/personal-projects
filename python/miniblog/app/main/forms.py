from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
import sqlalchemy as sa
from app.models import User
from flask_babel import _, lazy_gettext as _l


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username', validators=[DataRequired()]))
    about_me = TextAreaField(_l('About me', validators=[Length(min=0, max=140)]))
    submit = SubmitField(_l('Submit'))

    # validate username - confirm new username isn't already in use
    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == username.data))
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


# for submitting a blog post
class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something', validators=[
        DataRequired(), Length(min=1, max=140)]))
    submit = SubmitField(_l('Submit'))
    

# for submitting following and unfollowing actions
class EmptyForm(FlaskForm):
    submit = SubmitField(_l('Submit'))