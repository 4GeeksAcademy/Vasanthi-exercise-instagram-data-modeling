import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Users(Base):
    __tablename__= 'users'
    id= Column(Integer, primary_key=True)
    username= Column(String(250), nullable=False)
    role= Column(String(250), nullable=False)
    created_at=  Column(String(250), nullable=False)

class Follows(Base):
    __tablename__='follows'

    following_user_id  = Column(Integer, primary_key=True)
    created_at =  Column(String(250), nullable=False) 
    followed_user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship(Users)
    
    def serialize(self):
        return {

        }

class Likes(Base):
    __tablename__ = 'like'
    id= Column(Integer, primary_key=True)
    created_at=  Column(String(250), nullable=False)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship(Users)
    
    def serialize(self):
        return {

        }

class Comments(Base):
    __tablename__='comment'
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    description= Column(String(250), nullable=True)
    like_id= Column(Integer, ForeignKey('like.id'), nullable=True)
    created_at= Column(String(250), nullable=False)
    users = relationship(Users)
    like = relationship(Likes)
    def serialize(self):
        return {

        }

class Shares(Base):
    __tablename__='share'
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at=  Column(String(250), nullable=False)
    users = relationship(Users)
    
    def serialize(self):
        return {

        }

class Tags(Base):
    __tablename__='tag'
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship(Users)
    created_at=  Column(String(250), nullable=False)

    def serialize(self):
        return {

        }

class posts(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    title= Column(String(250), nullable=True)
    body= Column(String(250), nullable=True)
    location= Column(String(250), nullable=True)
    comments_id= Column(Integer, ForeignKey('comment.id'), nullable=True)
    save= Column(Boolean, nullable=True)
    like_id= Column(Integer, ForeignKey('like.id'), nullable=True)
    share_id= Column(Integer, ForeignKey('share.id'), nullable=True)
    tag_id= Column(Integer, ForeignKey('tag.id'), nullable=True)
    created_at= Column(String(250), nullable=False)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)

    comment = relationship(Comments)
    users = relationship(Users)
    tag = relationship(Tags)
    like = relationship(Likes)
    share = relationship(Shares)

    def serialize(self):
        return {
            "id": self.id,
            'title': self.title,
            'body': self.body,
            'location': self.location,
            'comments_id': self.comments_id,
            'save': self.save,
            'like_id': self.like_id,
            'share_id': self.share_id,
            'tag_id': self.tag_id,
            'created_at': self.created_at,
            'user_id': self.user_id      
       }
    
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
