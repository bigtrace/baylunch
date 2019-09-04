from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import Customer, Order
from app.users.forms import (RegisterForm, LoginForm,UpdateAccounForm)  #, ,resetRequestForm, resetPasswordForm)
from app.users.utils import save_pics

users = Blueprint('users', __name__)


@users.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form_obj  = RegisterForm()
    if form_obj.validate_on_submit():

        hashed_pwd = bcrypt.generate_password_hash(form_obj.password.data).decode('utf-8')
        user = Customer(phone=form_obj.phone.data,username=form_obj.username.data,password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has been created successfully.You can log in now','success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='register',form=form_obj)





@users.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form_obj  = LoginForm()
    if form_obj.validate_on_submit():

        customer = Customer.query.filter_by(phone = form_obj.phone.data).first()

        if customer and bcrypt.check_password_hash(customer.password,form_obj.password.data):
            login_user(customer,remember=form_obj.remember.data)
            next_page = request.args.get('next')
            flash('you have been logged in ','success')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('username or password or incorrect ','danger')

    return render_template('login.html', title='login',form=form_obj)






@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))



@users.route("/account",methods=['GET','POST'])
@login_required
def account():
    form_obj = UpdateAccounForm()

    if form_obj.validate_on_submit():

        if form_obj.picture.data:
            pic_name = save_pics(form_obj.picture.data)
            current_user.image_file = pic_name

        current_user.username = form_obj.username.data
        current_user.email = form_obj.email.data

        current_user.company = form_obj.company.data
        current_user.company_loc = form_obj.company_loc.data


        db.session.commit()
        flash(f'Account has been updated successfully','success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form_obj.username.data = current_user.username
        form_obj.email.data = current_user.email
        form_obj.company.data = current_user.company

        form_obj.company_loc.data = current_user.company_loc

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='account',image_file=image_file,form=form_obj)




#
#
#
# @users.route("/reset_password",methods=['GET','POST'])
# def reset_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home'))
#     form_obj = resetRequestForm()
#     if form_obj.validate_on_submit():
#
#         user = User.query.filter_by(email=form_obj.email.data).first()
#         if user is None:
#             flash('There is no account associated with this email','danger')
#         else:
#             send_reset_email(user)
#             flash('Reset password links has been sent out','success')
#
#     return render_template('reset_request.html', title='Reset Password', form=form_obj)
#
# @users.route("/reset_password/<token>",methods=['GET','POST'])
# def reset_token(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home'))
#     user = User.verify_token(token)
#     if user is None:
#         flash('token is invalid or has been expired','danger')
#         return redirect(url_for('users.reset_request'))
#     form_obj = resetPasswordForm()
#     if form_obj.validate_on_submit():
#         hashed_pwd = bcrypt.generate_password_hash(form_obj.password.data).decode('utf-8')
#         user.password=hashed_pwd
#         db.session.commit()
#         flash('Your password has been reset successfully','success')
#         return redirect(url_for('users.login'))
#     return render_template('reset_token.html', title='Reset Password', form=form_obj)
