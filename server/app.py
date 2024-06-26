#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Team, Player, MyTeam, PlayerStats, TeamStats


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
    
    def post(self):
        try:
            new_team = Team(
            name= request.json.get('name'),
            orign= request.json.get('orign'),
            conference= request.json.get('conference'),
            regularR= request.json.get('regularR'),
            playoffR= request.json.get('playoffR'),
            championships= request.json.get('championships'),
            titles= request.json.get('titles'),
            image= request.json.get('image'),
            coach= request.json.get('coach'),
            )
            db.session.add(new_team)
            db.session.commit()
            response_body = new_team.to_dict()
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "Team must have completed all inputs!"
            }
            return make_response(response_body, 400)
        
    
    
api.add_resource(AllTeams, '/teams')


class PlayerByID(Resource):
    def get(self, id):
        response_dict = Player.query.filter_by(id=id).first().to_dict()
        response = make_response(
            response_dict, 
            200
        )
        return response
    
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
    def get(self, id):
        team = Team.query.filter_by(id=id).first()
        if team:
            response_dict = team.to_dict()
            return make_response(response_dict, 200)
        else:
            return {"error": "Team not found"}, 404
        

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

class PlayerStatsResource(Resource):
    def get(self, player_id):
        player_stats = PlayerStats.query.filter_by(player_id=player_id).first()

        if player_stats:

            return player_stats.to_dict(), 200
        
        else:
            return {"error": "Player stats not found"}, 404

api.add_resource(PlayerStatsResource, '/players/<int:player_id>/stats')

class TeamStatsByTeamId(Resource):
    def get(self, team_id):
        team_stats = TeamStats.query.filter_by(team_id=team_id).first()

        if team_stats:
            return team_stats.to_dict(), 200
        
        else:
            return {"error": "Team stats not found"}, 404
        
api.add_resource(TeamStatsByTeamId, '/teams/<int:team_id>/stats')





class TeamPlayers(Resource):
    def get(self, team_id):
        team = Team.query.get(team_id)
        if team:
            players = [player.to_dict() for player in team.players]
            return players, 200
        else:
            return {"error": "Team not found"}, 404

api.add_resource(TeamPlayers, '/teams/<int:team_id>/players')



@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

