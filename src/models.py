import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table User.
    id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False)
    firstname = Column(String(15), nullable=False)
    lastname = Column(String(15), nullable=False)
    email = Column(String, unique=True)

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table Follower.
    user_from_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('User.id'), primary_key=True)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table Post.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table Comment.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship(Post)
    author_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table Media.
    id = Column(Integer, primary_key=True)
    types = Column(Enum('Analytics', 'Blogging', 'Business', 'Comunications', 'Copywriting', 'Digital_Marketing', 'Desing', 'Email _Marketing'), nullable=False)
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship(Post)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')