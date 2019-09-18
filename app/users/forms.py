from flask_wtf import FlaskForm,RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import Customer



class RegisterForm(FlaskForm):
    phone=StringField('Phone: (+1)',validators=[DataRequired(),Length(min=10,max=10)])
    username=StringField('Username',validators=[DataRequired(),Length(min=3,max=10)])
    #email=StringField('Email(Optional)',validators=[Email()])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('Comfirm your Password',validators=[DataRequired(),EqualTo('password')])
    #recaptcha = RecaptchaField()
    submit=SubmitField('Sign up')
    def validate_phone(self,phone):
        print('verify phone')
        customer = Customer.query.filter_by(phone=phone.data).first()
        if customer:
            raise ValidationError('This phone number has been taken,choose another phone number.')

    def validate_username(self,username):
        print('verify username')
        customer = Customer.query.filter_by(username=username.data).first()
        if customer:
            raise ValidationError('Username has been taken,choose another one.')



class LoginForm(FlaskForm):
    phone=StringField('Phone: (+1)',validators=[DataRequired(),Length(min=10,max=10)])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')
    remember = BooleanField('remember me')



class UpdateAccounForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=3,max=10)])
    email=StringField('Email',validators=[Email()])
    #company=StringField('Company',validators=[Length(min=2,max=10)])
    dropdown_list = [('Others','...'),('TD','TD'),('RBC','RBC'),('ScotiaBank','ScotiaBank'),('BMO','BMO'),('CIBC','CIBC'),('AGF','AGF')]
    preset_company = SelectField('Select your company', choices=dropdown_list, default=1)
    company = StringField('or type your company name manually', validators=[Length(min=2, max=10)])

    company_loc=StringField('Company Location',validators=[Length(min=3,max=20)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit=SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = Customer.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username has been taken,choose another one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Customer.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email has been taken,choose another one.')

#
# class resetRequestForm(FlaskForm):
#     email=StringField('Email',validators=[DataRequired(),Email()])
#     submit=SubmitField('Send Reset Link')
#
#
# class resetPasswordForm(FlaskForm):
#     password=PasswordField('password',validators=[DataRequired()])
#     confirm_password=PasswordField('Comfirm your Password',validators=[DataRequired(),EqualTo('password')])
#     submit=SubmitField('Update your password')
#
