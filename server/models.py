from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    height = db.Column(db.String, nullable=False)
    weight = db.Column(db.String, nullable=False)
    team = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    drafted = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    favorite = db.Column(db.Boolean, default=False)

    stats = db.relationship('PlayerStats')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
            'team': self.team,
            'number': self.number,
            'image': self.image,
            'birthday': self.birthday,
            'bio': self.bio,
            'drafted': self.drafted,
            'position': self.position,
            'favorite': self.favorite,
            'teams': [team.serialize_simple_with_players() for team in self.teams]
        }
    
    def serialize_simple(self):
        return {
            'id': self.id,
            'name': self.name
        }

    


class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    origin = db.Column(db.Integer, nullable=False)
    conference = db.Column(db.String, nullable=False)
    regularR = db.Column(db.String, nullable=False)
    playoffR = db.Column(db.String, nullable=False)
    championships = db.Column(db.Integer, nullable=False)
    titles = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)
    coach = db.Column(db.String, nullable=False, unique=True)
    favorite = db.Column(db.Boolean, default=False)


    stats = db.relationship('TeamStats')
    players = db.relationship('Player', secondary='player_teams')


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'origin': self.origin,
            'conference': self.conference,
            'regularR': self.regularR,
            'playoffR': self.playoffR,
            'championships': self.championships,
            'titles': self.titles,
            'image': self.image,
            'coach': self.coach,
            'favorite': self.favorite,
            'players': [player.serialize_simple() for player in self.players]
        }
    
    def serialize_simple(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def serialize_simple_with_players(self):
        return {
            'id': self.id,
            'name': self.name,
            'players': [player.serialize_simple() for player in self.players]
        }




class TeamStats(db.Model, SerializerMixin):
    __tablename__ = 'teamstats'

    id = db.Column(db.Integer, primary_key=True)
    wins = db.Column(db.Integer, nullable=False)
    loses = db.Column(db.Integer, nullable=False)
    cstanding = db.Column(db.String, nullable=False)
    points = db.Column(db.Float, nullable=False)
    assists = db.Column(db.Float, nullable=False)
    rebounds = db.Column(db.Float, nullable=False)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'wins': self.wins,
            'loses': self.loses,
            'cstanding': self.cstanding,
            'points': self.points,
            'assists': self.assists,
            'rebounds': self.rebounds,
            'team_id': self.team_id
        }

    @validates('team_id')
    def validate_id(self, key, value):
        if not value:
            raise ValueError(f"Team stat must have a team id")
        else:
            return value


class PlayerStats(db.Model, SerializerMixin):
    __tablename__ = 'playerstats'

    id = db.Column(db.Integer, primary_key=True)
    gp = db.Column(db.Integer, nullable=False)
    minpg = db.Column(db.Float, nullable=False)
    rebpg = db.Column(db.Float, nullable=False)
    ppg = db.Column(db.Float, nullable=False)
    apg = db.Column(db.Float, nullable=False)
    spg = db.Column(db.Float, nullable=False)
    bpg = db.Column(db.Float, nullable=False)
    tpg = db.Column(db.Float, nullable=False)
    fgpercentage = db.Column(db.Float, nullable=False)
    threepercentage = db.Column(db.Float, nullable=False)

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'gp': self.gp,
            'minpg': self.minpg,
            'rebpg': self.rebpg,
            'ppg': self.ppg,
            'apg': self.apg,
            'spg': self.spg,
            'bpg': self.bpg,
            'tpg': self.tpg,
            'fgpercentage': self.fgpercentage,
            'threepercentage': self.threepercentage,
            'player_id': self.player_id
        }

        
        
class MyTeam(db.Model, SerializerMixin):
    __tablename__ = 'myteam'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    height = db.Column(db.String)
    weight = db.Column(db.String)
    team = db.Column(db.String)
    number = db.Column(db.Integer)
    image = db.Column(db.String)
    birthday = db.Column(db.String)
    bio = db.Column(db.String)
    drafted = db.Column(db.String)
    position = db.Column(db.String)
    favorite = db.Column(db.Boolean, default=False)



    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
            'team': self.team,
            'number': self.number,
            'image': self.image,
            'birthday': self.birthday,
            'bio': self.bio,
            'drafted': self.drafted,
            'position': self.position,
            'favorite': self.favorite
        }
    
class PlayerTeam(db.Model, SerializerMixin):
    __tablename__ = 'player_teams'
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column( db.Integer, db.ForeignKey('players.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    role = db.Column(db.String) 

    @property
    def serialize(self):
        return{
            'role': self.role
        }

