from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app import db, login_manager
from flask_login import UserMixin






@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))


class Customer(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(20),unique=True,nullable=False)
    phone=db.Column(db.String(12),unique=True,nullable=False)
    company=db.Column(db.String(20),nullable=True)
    company_loc=db.Column(db.String(20),nullable=True)
    #email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    #password=db.Column(db.String(60),nullable=False)
    orders=  db.relationship('Order',backref='customer',lazy=True)
    def __repr__(self):
        return f"Customer('{self.username}','{self.phone}','{self.company}')"

    # def get_reset_token(self,expires_sec=600):
    #     s = Serializer(current_app.config['SECRET_KEY'],expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')
    #
    # @staticmethod
    # def verify_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)





class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    dish_name= db.Column(db.String(20),nullable=False)
    pickup = db.Column(db.String(20),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    notes=db.Column(db.Text,nullable=False)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'),nullable=False)

    def __repr__(self):
        return f"Order('{self.dish_name}','{self.pickup}','{self.notes}')"
