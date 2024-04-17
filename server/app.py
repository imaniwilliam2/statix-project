#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Team, Player, MyTeam


# Views go here!
class AllPlayers(Resource):

    def get(self): 
        rb = [player.to_dict() for player in Player.query.all()]
        return make_response(rb, 200)
    
    def post(self):
        try:
            new_player = Player(
            name= request.json.get('name'),
            height= request.json.get('height'),
            weight= request.json.get('weight'),
            team= request.json.get('team'),
            number= request.json.get('number'),
            image= request.json.get('image'),
            birthday= request.json.get('birthday'),
            bio= request.json.get('bio'),
            drafted= request.json.get('drafted'),
            position= request.json.get('position')
            )
            db.session.add(new_player)
            db.session.commit()
            response_body = new_player.to_dict()
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "Player must have an completed all inputs!"
            }
            return make_response(response_body, 400)
        
    
api.add_resource(AllPlayers, '/players')

class AllTeams(Resource):

    def get(self):
        rb = [team.to_dict() for team in Team.query.all()]
        return make_response(rb, 200)
    
api.add_resource(AllTeams, '/teams')


class PlayerByID(Resource):
    def delete(self, id):
        player = db.session.get(Player, id)

        if(player):
            db.session.delete(player)
            db.session.commit()
            response = {}
            return make_response(response, 204)
        else:
            response = {
                "error": "Player not found"
            }
            return make_response(response, 404)
        
    def patch(self, id):
        player = Player.query.filter(Player.id == id).first()

        if(player):
            try:
                for attr in request.json:
                    setattr(player, attr, request.json[attr])

                db.session.commit()
                response = player.to_dict()
                return make_response(response, 202)
            except:
                response = {
                    "errors": ["validation errors"]
                }
                return make_response(response, 400)
        else:
            response = {
                "error": "Player not found"
            }
            return make_response(response, 404)


        
api.add_resource(PlayerByID, '/players/<int:id>')

class TeamById(Resource):
    def patch(self, id):
        team = Team.query.filter(Team.id == id).first()

        if(team):
            try:
                for attr in request.json:
                    setattr(team, attr, request.json[attr])

                db.session.commit()
                response = team.to_dict()
                return make_response(response, 202)
            except:
                response = {
                    "errors": ["validation errors"]
                }
                return make_response(response, 400)
        else:
            response = {
                "error": "Team not found"
            }
            return make_response(response, 404)
        
api.add_resource(TeamById, '/teams/<int:id>')



class GetAllMyTeam(Resource):

    def get(self): 
        rb = [player.to_dict() for player in MyTeam.query.all()]
        return make_response(rb, 200)
    
    def post(self):
        try:
            new_team_player = MyTeam(
            name= request.json.get('name'),
            height= request.json.get('height'),
            weight= request.json.get('weight'),
            team= request.json.get('team'),
            number= request.json.get('number'),
            image= request.json.get('image'),
            birthday= request.json.get('birthday'),
            bio= request.json.get('bio'),
            drafted= request.json.get('drafted'),
            position= request.json.get('position')
            )
            db.session.add(new_team_player)
            db.session.commit()
            response_body = new_team_player.to_dict()
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "Player must have an completed all inputs!"
            }
            return make_response(response_body, 400)
        
    
api.add_resource(GetAllMyTeam, '/my-team')

class MyTeamPlayerByID(Resource):
    def delete(self, id):
        player = db.session.get(MyTeam, id)

        if(player):
            db.session.delete(player)
            db.session.commit()
            response = {}
            return make_response(response, 204)
        else:
            response = {
                "error": "Player not found"
            }
            return make_response(response, 404)
        
    def patch(self, id):
        player = MyTeam.query.filter(MyTeam.id == id).first()

        if(player):
            try:
                for attr in request.json:
                    setattr(player, attr, request.json[attr])

                db.session.commit()
                response = player.to_dict()
                return make_response(response, 202)
            except:
                response = {
                    "errors": ["validation errors"]
                }
                return make_response(response, 400)
        else:
            response = {
                "error": "Player not found"
            }
            return make_response(response, 404)
        

api.add_resource(MyTeamPlayerByID, '/my-team/<int:id>')














@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

