#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Player


# Views go here!
class AllPlayers(Resource):

    def get(self): 
        rb = [player.to_dict() for player in Player.query.all()]
        return make_response(rb, 200)
    
api.add_resource(AllPlayers, '/players')


@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

