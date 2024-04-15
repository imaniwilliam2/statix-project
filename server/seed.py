#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Player

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        Player.query.delete()

        print("Starting seed...")

        player1 = Player(name='Lebron James',
                        height="6'9",
                        weight='250', 
                        team='Los Angeles Lakers',
                        number='23',
                        age='39',
                        image='/assets/lebron_james.jpeg',
                        birthday='December 10, 1984',
                        bio='From Akron Ohio, LeBron has averaged 27.1 points, 7.5 rebounds, and 7.4 assists in 1,490 regular-season games. LeBron James has played 21 seasons for the Cavaliers, Lakers and Heat.',
                        drafted='2003 Rnd 1, Pick 1 by CLE',
                        position='Small Forward')
        
        db.session.add(player1)
        db.session.commit()

        # Seed code goes here! 
        print("Completed seeding!")

