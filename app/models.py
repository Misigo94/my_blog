from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__="users"
    # Password is a string nullable = required username should be unique unique
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy="dynamic")
    comments = db.relationship('Comment', backref='user', lazy="dynamic")
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    # Our function forsaving the user objects
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Our function for deleting  
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Create a password for the user on sign up
    def set_password(self, password):
        # We intend to get the password as a hash from the text they get
        password_hash=generate_password_hash(password)
        # save the password hash
        self.password=password_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User: {self.username} <Email : {self.email}>"

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

class Post(db.Model):
    __tablename__="posts"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String)
    description = db.Column(db.String)
    author = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitchcomment = db.relationship('Comment', backref='post', lazy="dynamic")

    # Our function for deleting  
    def deletepost(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    # Our function for deleting  
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post('{self.date_posted}')"

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews

    # class Blogg(db.Model):
    #     __tablename__ = 'blogs'
    #     id = db.Column(db.Integer,primary_key=True)
    #     category = db.Column(db.Text, nullable=False)
    #     text = db.Column(db.Text, nullable=False)
    #     author = db.Column(db.Text, nullable=False)
    #     author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #     post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)