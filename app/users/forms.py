from flask_wtf import FlaskForm,RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User



class RegisterForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=5,max=10)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('Comfirm your Password',validators=[DataRequired(),EqualTo('password')])
    recaptcha = RecaptchaField()
    submit=SubmitField('Sign up')
    def validate_username(self,username):
    	user = User.query.filter_by(username=username.data).first()
    	if user:
    		raise ValidationError('Username has been taken,choose another one.')
    def validate_email(self,email):
    	user = User.query.filter_by(email=email.data).first()
    	if user:
    		raise ValidationError('Email has been taken,choose another one.')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')
    remember = BooleanField('remember me')



class UpdateAccounForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=5,max=10)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit=SubmitField('Update')
    def validate_username(self,username):
    	if username.data != current_user.username:
	    	user = User.query.filter_by(username=username.data).first()
	    	if user:
	    		raise ValidationError('Username has been taken,choose another one.')
    def validate_email(self,email):
    	if email.data != current_user.email:
	    	user = User.query.filter_by(email=email.data).first()
	    	if user:
	    		raise ValidationError('Email has been taken,choose another one.')



class resetRequestForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Send Reset Link')


class resetPasswordForm(FlaskForm):
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('Comfirm your Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Update your password')

