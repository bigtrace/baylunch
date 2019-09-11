
from flask import request,render_template,url_for,flash,redirect,abort,Blueprint
from app.orders.forms import OrderForm
from app import db
from app.models import Customer,Order
from flask_login import current_user,login_required


orders =Blueprint('posts',__name__)

# view post
@orders.route("/order/<int:order_id>")
def post(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('post.html', title=order.dish_name, order=order)


# create post
@orders.route("/orders/new",methods=['GET','POST'])
@login_required
def new_post():
    form_obj = OrderForm()
    if form_obj.validate_on_submit():
        post = Order(title =form_obj.title.data,content= form_obj.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Post has been created successfully','success')
        return redirect(url_for('main.home'))

    return render_template('create_post.html', title='New Post',legend='Create Post',form=form_obj)
#
# # update post
# @posts.route("/post/<int:post_id>/update",methods=['GET','POST'])
# @login_required
# def update_post(post_id):
#     form_obj = PostForm()
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#
#     if form_obj.validate_on_submit():
#         post.title = form_obj.title.data
#         post.content = form_obj.content.data
#         db.session.commit()
#         flash(f'Post has been updated successfully','success')
#         return redirect(url_for('posts.post',post_id = post.id))
#     elif request.method == 'GET':
#         form_obj.title.data = post.title
#         form_obj.content.data = post.content
#     return render_template('create_post.html', title='Update Post', form=form_obj,legend='Update Post')
#
# # delete post
# @posts.route("/post/<int:post_id>/delete",methods=['GET','POST'])
# @login_required
# def delete_post(post_id):
#
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     else:
#         db.session.delete(post)
#         db.session.commit()
#         flash(f'Post has been deleted successfully','success')
#         return redirect(url_for('main.home'))
#
# @posts.route("/user/<string:username>")
# def user_post(username):
#     user = User.query.filter_by(username = username).first_or_404()
#     page = request.args.get('page',1,type=int)
#     posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
#     return render_template('user_post.html',posts=posts,user=user)
