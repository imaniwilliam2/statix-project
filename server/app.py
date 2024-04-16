#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Team, Player


# Views go here!
class AllPlayers(Resource):

    def get(self): 
        rb = [player.to_dict() for player in Player.query.all()]
        return make_response(rb, 200)
    
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






@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

