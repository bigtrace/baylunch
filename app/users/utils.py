import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from app import mail



def save_pics(form_img_data):
    random_hex = secrets.token_hex(8)
    _,ext = os.path.splitext(form_img_data.filename)
    filename = random_hex+ext
    full_path = os.path.join(current_app.root_path,'static/profile_pics',filename)

    resize_img= Image.open(form_img_data)
    resize_img.thumbnail((125,125))
    resize_img.save(full_path)
    return filename


#
# def send_reset_email(user):
#
#     token = user.get_reset_token()
#     msg = Message('Password Reset Request',
#                   sender='caia.bigtrace@gmail.com',
#                   recipients=[user.email])
#     msg.body = f'''To reset your password, visit the following link:
# {url_for('users.reset_token', token=token, _external=True)}
# If you did not make this request then simply ignore this email and no changes will be made.
# '''
#     mail.send(msg)
