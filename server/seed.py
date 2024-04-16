#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Team, Player

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        Player.query.delete()
        Team.query.delete()

        print("Starting seed...")

        team1 = Team(
            name="Los Angeles Lakers",
            origin=1948,
            conference="Western",
            regularR="3550-2454",
            playoffR="466-314",
            championships=17,
            titles=19,
            image="/assets/lakers.jpeg",
            coach="Darvin Ham")
        
        team2 = Team(
            name="Golden State Warriors",
            origin=1946,
            conference="Western",
            regularR="2969-3134",
            playoffR="212-172",
            championships=7,
            titles=7,
            image="/assets/warriors.png",
            coach="Steve Kerr")
        
        db.session.add_all([team1, team2])
        db.session.commit()


        player1 = Player(name='Lebron James',
                        height="6'9",
                        weight="250", 
                        team=team1.id,
                        number=23,
                        image='/assets/lebron_james.jpeg',
                        birthday='December 10, 1984 (39)',
                        bio='From Akron, Ohio, LeBron has averaged 27.1 points, 7.5 rebounds, and 7.4 assists in 1,490 regular-season games. LeBron James has played 21 seasons for the Cavaliers, Lakers and Heat.',
                        drafted='2003 Rnd 1, Pick 1 by CLE',
                        position='Small Forward',
                        )
        

        player2 = Player(name="D'Angelo Russell",
                        height="6'3",
                        weight="193", 
                        team=team1.id,
                        number=1,
                        image="/assets/d'angelo.jpeg",
                        birthday='February 23, 1996 (28)',
                        bio="From Louisville, Kentucky, D'Angelo Russel has averaged 17.8 points, 3.4 rebounds, and 5.8 assists in 571 regular-season games. D'Angelo has played 9 seasons for 4 teams including the Lakers and Timberwolves.",
                        drafted='2015 Rnd 1, Pick 2 by LAL',
                        position='Point Guard',
                        )
        
        db.session.add_all([player1, player2])
        db.session.commit() 



        # Seed code goes here! 
        print("Completed seeding!")

