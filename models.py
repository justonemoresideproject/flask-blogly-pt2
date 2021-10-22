"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

def connect_db(app):
        db.app = app
        db.init_app(app)

class User(db.Model):
    """User class"""

    __tablename__ = "users"
    
    @property
    def represent(self):
        p = self
        return f"<id={p.id} first name={p.first_name} last name={p.last_name} image_url={p.image_url}>"

    @property
    def get_full_name(self):
        p = self
        return f"{p.first_name} {p.last_name}"

    id = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)
    first_name = db.Column(db.Text,
            nullable=False,
            unique=False)
    last_name = db.Column(db.Text,
            nullable=False,
            unique=False)
    image_url = db.Column(db.String(255),
            unique=False, default=DEFAULT_IMAGE_URL)
    posts = db.Column(db.Integer, db.ForeignKey('posts.id'))

    posts = db.relationship('Post', backref='user')

class Post(db.Model):
    """Posts Class"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)
    title = db.Column(db.Text,
        nullable=False,
        unique=False)
    comment = db.Column(db.Text,
        nullable=False,
        unique=False)
    posted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_made = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)

    @property
    def friendly_date(self):
            return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")


