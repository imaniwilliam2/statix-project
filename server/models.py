from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    height = db.Column(db.String, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    age  = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    drafted = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)

    # team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    
