#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Team, Player, PlayerStats, TeamStats, PlayerTeam

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        Player.query.delete()
        Team.query.delete()
        TeamStats.query.delete()
        PlayerStats.query.delete()

        print("Starting seed...")

        team1 = Team(
            name="Los Angeles Lakers",
            origin=1948,
            conference="Western",
            regularR="3550-2454",
            playoffR="466-314",
            championships=17,
            titles=19,
            image="/assets/teams/lakers.png",
            coach="Darvin Ham")
        
        team2 = Team(
            name="Golden State Warriors",
            origin=1946,
            conference="Western",
            regularR="2969-3134",
            playoffR="212-172",
            championships=7,
            titles=7,
            image="/assets/teams/gsw.webp",
            coach="Steve Kerr")
        
        team3 = Team(
            name="Boston Celtics",
            origin=1946,
            conference="Eastern",
            regularR="3634-2480",
            playoffR="407-312",
            championships=17,
            titles=10,
            image="/assets/teams/celtics.png",
            coach="Joe Mazzulla")
        
        team4 = Team(
            name="Cleveland Cavaliers",
            origin=1970,
            conference="Eastern",
            regularR="2032-2321",
            playoffR="126-108",
            championships=1,
            titles=5,
            image="/assets/teams/cavs.png",
            coach="J.B. Bickerstaff")
        
        team5 = Team(
            name="Orland Magic",
            origin=1989,
            conference="Eastern",
            regularR="1315-1488",
            playoffR="59-74",
            championships=0,
            titles=2,
            image="/assets/teams/magic.png",
            coach="Jamahl Mosley")
        
        team6 = Team(
            name="Milwaukee Bucks",
            origin=1968,
            conference="Eastern",
            regularR="2389-2136",
            playoffR="150-156",
            championships=2,
            titles=3,
            image="/assets/teams/bucks.png",
            coach="Doc Rivers")
        
        team7 = Team(
            name="Indiana Pacers",
            origin=1976,
            conference="Eastern",
            regularR="1930-1938",
            playoffR="115-126",
            championships=0,
            titles=1,
            image="/assets/teams/pacers.svg",
            coach="Rick Carlisle")
        
        team8 = Team(
            name="New York Knicks",
            origin=1946,
            conference="Eastern",
            regularR="2974-3131",
            playoffR="193-198",
            championships=2,
            titles=4,
            image="/assets/teams/knicks.png",
            coach="Tom Thibodeau")
        
        team9 = Team(
            name="Chicago Bulls",
            origin=1966,
            conference="Eastern",
            regularR="2383-2297",
            playoffR="187-162",
            championships=6,
            titles=6,
            image="/assets/teams/bulls.png",
            coach="Billy Donovan")
        
        team10 = Team(
            name="Atlanta Hawks",
            origin=1949,
            conference="Eastern",
            regularR="2927-3010",
            playoffR="170-223",
            championships=1,
            titles=0,
            image="/assets/teams/hawks.png",
            coach="Quin Snyder")
        
        team11 = Team(
            name="Philadelphia 76ers",
            origin=1949,
            conference="Eastern",
            regularR="3101-2840",
            playoffR="249-234",
            championships=3,
            titles=5,
            image="/assets/teams/76ers.png",
            coach="Nick Nurse")
        
        team12 = Team(
            name="Miami Heat",
            origin=1988,
            conference="Eastern",
            regularR="1521-1364",
            playoffR="162-128",
            championships=3,
            titles=7,
            image="/assets/teams/heat.png",
            coach="Eric Spoelstra")
        
        team13 = Team(
            name="Oklahoma City Thunder",
            origin=1976,
            conference="Western",
            regularR="2470-2136",
            playoffR="164-167",
            championships=1,
            titles=4,
            image="/assets/teams/thunder.png",
            coach="Mark Daigneault")
        
        team14 = Team(
            name="L.A. Clippers",
            origin=1976,
            conference="Western",
            regularR="1843-2517",
            playoffR="64-83",
            championships=0,
            titles=0,
            image="/assets/teams/clippers.png",
            coach="Tyronn Lue")
        
        team15 = Team(
            name="Dallas Mavericks",
            origin=1980,
            conference="Western",
            regularR="1797-1746",
            playoffR="105-122",
            championships=1,
            titles=2,
            image="/assets/teams/mavericks.png",
            coach="Jason Kidd")
        
        team16 = Team(
            name="Minnesota Timberwolves",
            origin=1989,
            conference="Western",
            regularR="1147-1647",
            playoffR="21-42",
            championships=0,
            titles=0,
            image="/assets/teams/timberwolves.png",
            coach="Chris Finch")
        
        team17 = Team(
            name="Phoenix Suns",
            origin=1968,
            conference="Western",
            regularR="2429-2096",
            playoffR="160-160",
            championships=0,
            titles=3,
            image="/assets/teams/suns.png",
            coach="Frank Vogel")
        
        team18 = Team(
            name="Denver Nuggets",
            origin=1976,
            conference="Western",
            regularR="1954-1915",
            playoffR="98-132",
            championships=1,
            titles=1,
            image="/assets/teams/nuggets.png",
            coach="Michael Malone")
        
        team19 = Team(
            name="Sacramento Kings",
            origin=1948,
            conference="Western",
            regularR="2748-3257",
            playoffR="83-112",
            championships=1,
            titles=0,
            image="/assets/teams/kings.png",
            coach="Mike Brown")
        

        team20 = Team(
            name="New Orleans Pelicans",
            origin=2002,
            conference="Western",
            regularR="831-937",
            playoffR="22-33",
            championships=0,
            titles=0,
            image="/assets/teams/pelicans.svg",
            coach="Willie Green")


        
        db.session.add_all([team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14, team15, team16, team17, team18, team19, team20])
        db.session.commit()


        team_stats1 = TeamStats(wins=47,
                                loses=35,
                                cstanding="7th",
                                points=118.0,
                                assists=28.5,
                                rebounds=43.1,
                                team_id=1,
        )
        team_stats2 = TeamStats(wins=46,
                                loses=36,
                                cstanding="10th",
                                points=117.8,
                                assists=29.3,
                                rebounds=46.7,
                                team_id=2,
        )
        team_stats3 = TeamStats(wins=64,
                                loses=18,
                                cstanding="1st",
                                points=120.6,
                                assists=26.9,
                                rebounds=46.3,
                                team_id=3,
        )
        team_stats4 = TeamStats(wins=48,
                                loses=34,
                                cstanding="4th",
                                points=112.6,
                                assists=28.0,
                                rebounds=43.3,
                                team_id=4,
        )
        team_stats5 = TeamStats(wins=47,
                                loses=35,
                                cstanding="5th",
                                points=110.5,
                                assists=24.7,
                                rebounds=42.3,
                                team_id=5,
        )
        team_stats6 = TeamStats(wins=49,
                                loses=33,
                                cstanding="3rd",
                                points=119.0,
                                assists=26.5,
                                rebounds=44.2,
                                team_id=6,
        )
        team_stats7 = TeamStats(wins=47,
                                loses=35,
                                cstanding="6th",
                                points=123.3,
                                assists=30.8,
                                rebounds=31.5,
                                team_id=7,
        )
        team_stats8 = TeamStats(wins=50,
                                loses=32,
                                cstanding="2nd",
                                points=112.8,
                                assists=24.4,
                                rebounds=45.2,
                                team_id=8,
        )
        team_stats9 = TeamStats(wins=39,
                                loses=43,
                                cstanding="9th",
                                points=112.3,
                                assists=25.0,
                                rebounds=43.8,
                                team_id=9,
        )
        team_stats10 = TeamStats(wins=36,
                                loses=46,
                                cstanding="10th",
                                points=118.3,
                                assists=26.6,
                                rebounds=44.7,
                                team_id=10,
        )
        team_stats11 = TeamStats(wins=47,
                                loses=35,
                                cstanding="7th",
                                points=114.6,
                                assists=24.9,
                                rebounds=43.0,
                                team_id=11,
        )
        team_stats12 = TeamStats(wins=46,
                                loses=36,
                                cstanding="8th",
                                points=110.1,
                                assists=25.8,
                                rebounds=42.3,
                                team_id=12,
        )
        team_stats13 = TeamStats(wins=57,
                                loses=25,
                                cstanding="1st",
                                points=120.1,
                                assists=27.1,
                                rebounds=42.0,
                                team_id=13,
        )
        team_stats14 = TeamStats(wins=51,
                                loses=31,
                                cstanding="4th",
                                points=115.6,
                                assists=25.6,
                                rebounds=43.0,
                                team_id=14,
        )
        team_stats15 = TeamStats(wins=50,
                                loses=32,
                                cstanding="5th",
                                points=117.9,
                                assists=25.7,
                                rebounds=42.9,
                                team_id=15,
        )
        team_stats16 = TeamStats(wins=56,
                                loses=26,
                                cstanding="3rd",
                                points=113.0,
                                assists=26.6,
                                rebounds=43.6,
                                team_id=16,
        )
        team_stats17 = TeamStats(wins=49,
                                loses=33,
                                cstanding="6th",
                                points=116.2,
                                assists=27.0,
                                rebounds=44.1,
                                team_id=17,
        )
        team_stats18 = TeamStats(wins=57,
                                loses=25,
                                cstanding="2nd",
                                points=114.9,
                                assists=29.4,
                                rebounds=44.4,
                                team_id=18,
        )
        team_stats19 = TeamStats(wins=46,
                                loses=36,
                                cstanding="9th",
                                points=116.6,
                                assists=28.3,
                                rebounds=44.0,
                                team_id=19,
        )
        team_stats20 = TeamStats(wins=49,
                                loses=33,
                                cstanding="8th",
                                points=115.1,
                                assists=27.0,
                                rebounds=44.0,
                                team_id=20,
        )

        
        db.session.add_all([team_stats1, team_stats2, team_stats3, team_stats4, team_stats5, team_stats6, team_stats7, team_stats8, team_stats9, team_stats10, team_stats11, team_stats12, team_stats13, team_stats14, team_stats15, team_stats16, team_stats17, team_stats18, team_stats19, team_stats20])
        db.session.commit()






        player1 = Player(name='Lebron James',
                        height="6'9",
                        weight="250", 
                        team=team1.id,
                        number=23,
                        image="/assets/teams/lebron.webp",
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
                        image="/assets/players/d'angelo.webp",
                        birthday='February 23, 1996 (28)',
                        bio="From Louisville, Kentucky, D'Angelo Russel has averaged 17.8 points, 3.4 rebounds, and 5.8 assists in 571 regular-season games. D'Angelo has played 9 seasons for 4 teams including the Lakers and Timberwolves.",
                        drafted='2015 Rnd 1, Pick 2 by LAL',
                        position='Point Guard',
                        )
        
        player3 = Player(name="Anthony Davis",
                        height="6'10",
                        weight="253", 
                        team=team1.id,
                        number=3,
                        image="/assets/players/davis.webp",
                        birthday='March 11, 1993 (31)',
                        bio="From Kentucky, Anthony Davis has averaged 24.1 points, 10.6 rebounds, and 2.5 assists in 736 regular-season games. Davis has played 12 seasons for the Lakers and Pelicans as well as has been selected to play in 8 All-Star games.",
                        drafted='2012 Rnd 1, Pick 1 by NOH',
                        position='Power Forward',
                        )
        
        player4 = Player(name="Austin Reaves",
                        height="6'5",
                        weight="197", 
                        team=team1.id,
                        number=15,
                        image="/assets/players/reaves.webp",
                        birthday='May 29, 1998 (25)',
                        bio="From Oklahoma, Austin has averaged 12.4 points, 2.6 rebounds, and 3.7 assists in 207 regular-season games. Reaves has played 3 seasons for the Lakers.",
                        drafted='Undrafted',
                        position='Shooting Guard',
                        )
        
        player5 = Player(name="Taurean Prince",
                        height="6'6",
                        weight="218", 
                        team=team1.id,
                        number=12,
                        image="/assets/players/prince.png",
                        birthday='March 22, 1994 (30)',
                        bio="From Baylor, Taurean Prince has averaged 10.1 points, 3.6 rebounds in 502 regular-season games. Prince has played 8 seasons for 5 teams including the Lakers, Timberwolves, and Hawks.",
                        drafted='2016, Rnd 1, Pick 12 by UTA',
                        position='Power Forward',
                        )
        
        # Warriors
        player6 = Player(name="Stephen Curry",
                        height="6'2",
                        weight="185", 
                        team=team2.id,
                        number=30,
                        image="/assets/players/curry.webp",
                        birthday='March 14, 1988 (36)',
                        bio="From Davidson, Stephen Curry has averaged 24.8 points, 6.4 assists, and 4.7 rebounds in 956 regular-season games. Curry has played 15 seasons for the Warriors, selected to play 9 All-Star games, and 3 MVP awards.",
                        drafted='2009, Rnd 1, Pick 7 by GSW',
                        position='Point Guard',
                        )
        
        player7 = Player(name="Klay Thompson",
                        height="6'6",
                        weight="220", 
                        team=team2.id,
                        number=11,
                        image="/assets/players/klay.avif",
                        birthday='February 8, 1990 (34)',
                        bio="From Washington State, Thompson has averaged 19.6 points, 2.3 assists, and 3.5 rebounds in 793 regular-season games. Klay has played 11 seasons for the Warriors and has been selected to play 5 All-Star games.",
                        drafted='2011 Rnd 1, Pick 11 by GSW',
                        position='Shooting Guard',
                        )
        
        player8 = Player(name="Andrew Wiggins",
                        height="6'7",
                        weight="197", 
                        team=team2.id,
                        number=22,
                        image="/assets/players/wiggins.avif",
                        birthday='February 23, 1995 (29)',
                        bio="From Kansas, Andrew Wiggins has averaged 18.5 points, 2.3 assists, and 4.5 rebounds in 706 regular-season games. Wiggins has played 10 seasons for the Warriors and Timberwolves, has been selected to play 1 All-Star game, and won the Rookie of the Year Award.",
                        drafted='2014 Rnd 1, Pick 1 by CLE',
                        position='Small Forward',
                        )
        
        player9 = Player(name="Draymond Green",
                        height="6'6",
                        weight="230", 
                        team=team2.id,
                        number=11,
                        image="/assets/players/draymond.avif",
                        birthday='March 4, 1990 (34)',
                        bio="From Michigan State, Draymond Green has averaged 8.7 points, 5.6 assists, and 7.0 rebounds in 813 regular-season games. Draymond has played 12 seasons for the Warriors, has been selected to play 4 All-Star games, and has won 1 Defensive Player of the Year award.",
                        drafted='2012 Rnd 2, Pick 35 by GSW',
                        position='Power Forward',
                        )
        
        player10 = Player(name="Kevon Looney",
                        height="6'9",
                        weight="222", 
                        team=team2.id,
                        number=5,
                        image="/assets/players/looney.avif",
                        birthday='February 6, 1996 (28)',
                        bio="From UCLA, Looney has averaged 5.0 points, and 5.6 rebounds in 523 regular-season games. Kevon Looney has played 9 seasons for the Warriors.",
                        drafted='2015 Rnd 1, Pick 30 by GSW',
                        position='Power Forward',
                        )
        
        # Celtics
        player11 = Player(name="Jrue Holiday",
                        height="6'4",
                        weight="205", 
                        team=team3.id,
                        number=4,
                        image="/assets/players/drue.png",
                        birthday='June 12, 1990 (33)',
                        bio="From UCLA, Jrue Holiday has averaged 16.1 points, 6.4 assists, and 4.2 rebounds in 975 regular-season games. Kevon Looney has played 15 seasons for 4 teams including the Pelicans and Bucks, and has been selected to play 2 All-Star games.",
                        drafted='2009 Rnd 1, Pick 17 by PHI',
                        position='Point Guard',
                        )
        
        player12 = Player(name="Derrick White",
                        height="6'4",
                        weight="190", 
                        team=team3.id,
                        number=9,
                        image="/assets/players/white.webp",
                        birthday='July 2, 1994 (29)',
                        bio="From Colorado, Derrick White has averaged 12.3 points, 4.1 assists, and 3.5 rebounds in 418 regular-season games. Derrick has played 7 seasons for the Spurs and Celtics.",
                        drafted='2017 Rnd 1, Pick 29 by SAS',
                        position='Shooting Guard',
                        )
        
        player13 = Player(name="Jaylen Brown",
                        height="6'6",
                        weight="223", 
                        team=team3.id,
                        number=7,
                        image="/assets/players/jaylen.avif",
                        birthday='October 24, 1996 (27)',
                        bio="From California, Jaylen Brown has averaged 18.6 points, 2.4 assists, and 5.3 rebounds in 540 regular-season games. Brown has played 8 seasons for the Celtics, and has been selected to play 2 All-Star games.",
                        drafted='2016 Rnd 1, Pick 3 by BOS',
                        position='Small Forward',
                        )

        player14 = Player(name="Jayson Tatum",
                        height="6'8",
                        weight="210", 
                        team=team3.id,
                        number=0,
                        image="/assets/players/jayson.webp",
                        birthday='March 3, 1998 (26)',
                        bio="From Duke, Jayson Tatum has averaged 23.1 points, 3.5 assists, and 7.2 rebounds in 513 regular-season games. Jayson has played 7 seasons for the Celtics, and has been selected to play 4 All-Star games.",
                        drafted='2017 Rnd 1, Pick 3 by BOS',
                        position='Small Forward',
                        )
        
        player15 = Player(name="Kristaps Porzingis",
                        height="7'2",
                        weight="240", 
                        team=team3.id,
                        number=8,
                        image="/assets/players/kris.png",
                        birthday='August 2, 1995 (28)',
                        bio="From Latvia, Porzingis has averaged 19.7 points, and 7.9 rebounds in 459 regular-season games. Kristaps has played 8 seasons for 4 teams including the Mavericks and Knicks, and has been selected to play 1 All-Star game.",
                        drafted='2017 Rnd 1, Pick 3 by BOS',
                        position='Power Forward',
                        )
        



        # Cavs
        player16 = Player(name="Daris Garland",
                        height="6'1",
                        weight="192", 
                        team=team4.id,
                        number=10,
                        image="/assets/players/daris.png",
                        birthday='January 26, 2000 (24)',
                        bio="From Vanderbilt, Daris Garland has averaged 18.4 points, 6.7 assists, and 2.6 rebounds in 307 regular-season games. Daris Garland has played 5 seasons for the Cavaliers, and has been selected to play 1 All-Star games.",
                        drafted='2019 Rnd 1, Pick 5 by CLE',
                        position='Point Guard',
                        )
        
        player17 = Player(name="Donavan Mitchell",
                        height="6'3",
                        weight="215", 
                        team=team4.id,
                        number=45,
                        image="/assets/players/donovan.avif",
                        birthday='September 7, 1996 (27)',
                        bio="From New York, Donavan has averaged 24.8 points, 4.6 assists, and 4.3 rebounds in 468 regular-season games. Mitchell has played 7 seasons for the Jazz and Cavaliers.",
                        drafted='2017 Rnd 1, Pick 13 by DEN',
                        position='Shooting Guard',
                        )
        
        player18 = Player(name="Caris LeVert",
                        height="6'6",
                        weight="205", 
                        team=team4.id,
                        number=3,
                        image="/assets/players/levert.png",
                        birthday='August 25, 1994 (29)',
                        bio="From Ohio, Caris LeVert has averaged 14.1 points, 4.1 assists, and 3.9 rebounds in 460 regular-season games. Brown has played 8 seasons for the Nets, Cavaliers, and Pacers.",
                        drafted='2016 Rnd 1, Pick 20 by IND',
                        position='Small Forward',
                        )

        player19 = Player(name="Evan Mobley",
                        height="6'11",
                        weight="215", 
                        team=team4.id,
                        number=4,
                        image="/assets/players/evan.avif",
                        birthday='June 18, 2001 (22)',
                        bio="From California, Mobley has averaged 15.6 points, 8.8 assists, and 2.9 rebounds in 198 regular-season games. Evan Mobley has played 3 seasons for the Cavaliers.",
                        drafted='2021 Rnd 1, Pick 3 by CLE',
                        position='Power Forward',
                        )
        
        player20 = Player(name="Jarrett Allen",
                        height="6'9",
                        weight="243", 
                        team=team4.id,
                        number=31,
                        image="/assets/players/allen.png",
                        birthday='April 21, 1998 (25)',
                        bio="From Texas, Jarrett Allen has averaged 12.7 points, and 9.1 rebounds in 486 regular-season games. Jarrett has played 8 seasons for the Cavaliers and Nets, and has been selected to play 1 All-Star game.",
                        drafted='2017 Rnd 1, Pick 22 by BKN',
                        position='Center',
                        )
        
        #  Magic
        player21 = Player(name="Cole Anthony",
                        height="6'2",
                        weight="185", 
                        team=team5.id,
                        number=50,
                        image="/assets/players/cole.avif",
                        birthday='May 15, 2000 (23)',
                        bio="From Portland, Anthony has averaged 13.4 points, 4.6 assists, and 4.1 rebounds in 253 regular-season games. Cole Anthony has played 4 seasons for the Magic.",
                        drafted='2020 Rnd 1, Pick 15 by ORL',
                        position='Point Guard',
                        )
        
        player22 = Player(name="Jalen Suggs",
                        height="6'5",
                        weight="205", 
                        team=team5.id,
                        number=4,
                        image="/assets/players/suggs.avif",
                        birthday='June 3, 2001 (22)',
                        bio="From St. Paul, Jalen Suggs has averaged 11.5 points, 3.2 assists, and 3.2 rebounds in 176 regular-season games. Suggs has played 3 seasons for the Magic.",
                        drafted='2021 Rnd 1, Pick 5 by ORL',
                        position='Shooting Guard',
                        )
        
        player23 = Player(name="Franz Wagner",
                        height="6'10",
                        weight="220", 
                        team=team5.id,
                        number=22,
                        image="/assets/players/franz.avif",
                        birthday='August 27, 2001 (22)',
                        bio="From Germany, Franz has averaged 17.8 points, 3.4 assists, and 4.6 rebounds in 231 regular-season games. Franz has played 3 seasons for the Magic.",
                        drafted='2021 Rnd 1, Pick 8 by ORL',
                        position='Small Forward',
                        )

        player24 = Player(name="Paolo Banchero",
                        height="6'10",
                        weight="250", 
                        team=team5.id,
                        number=5,
                        image="/assets/players/paolo.avif",
                        birthday='November 12, 2002 (21)',
                        bio="From Seattle, Paolo has averaged 21.3 points, 4.6 assists, and 6.9 rebounds in 152 regular-season games. Banchero has played 2 seasons for the Magic. He has the won Rookie of the Year award.",
                        drafted='2022 Rnd 1, Pick 1 by ORL',
                        position='Power Forward',
                        )
        
        player25 = Player(name="Wendell Carter Jr.",
                        height="6'10",
                        weight="270", 
                        team=team5.id,
                        number=34,
                        image="/assets/players/wendall.avif",
                        birthday='April 16, 1999 (25)',
                        bio="From Atlanta, Wendall Carter Jr. has averaged 12.5 points, 2.0 assists, and 8.5 rebounds in 315 regular-season games. Wendall has played 6 seasons for the Magic and Bulls.",
                        drafted='2017 Rnd 1, Pick 22 by BKN',
                        position='Center',
                        )
        
        # Bucks
        player26 = Player(name="Damian Lillard",
                        height="6'2",
                        weight="195", 
                        team=team6.id,
                        number=0,
                        image="/assets/players/damian.avif",
                        birthday='July 15, 1990 (33)',
                        bio="From Oakland, Damian has averaged 25.1 points, 6.7 assists, 6.7 assists, and 4.2 rebounds in 842 regular-season games. Lillard has played 12 seasons for the Trail Blazers and Bucks. He has the won Rookie of the Year award and been selected to play 7 All-Star games..",
                        drafted='2012 Rnd 1, Pick 6 by POR',
                        position='Point Guard',
                        )
        
        player27 = Player(name="Malik Beasley",
                        height="6'4",
                        weight="187", 
                        team=team6.id,
                        number=5,
                        image="/assets/players/malik.png",
                        birthday='November 26, 1996 (27)',
                        bio="From Atlanta, Beasley has averaged 10.9 points and 2.8 rebounds in 496 regular-season games. Malik Beasley has played 8 seasons for 5 teams including the Timberwolves and Nuggets.",
                        drafted='2016 Rnd 1, Pick 19 by DEN',
                        position='Shooting Guard',
                        )
        
        player28 = Player(name="Khris Middleton",
                        height="6'7",
                        weight="222", 
                        team=team6.id,
                        number=22,
                        image="/assets/players/khris.webp",
                        birthday='August 12, 1991 (32)',
                        bio="From Charleston, Middleton has averaged 16.9 points, 3.9 assists, and 4.8 rebounds in 739 regular-season games. Middleton has played 12 seasons for the Bucks and Pistons and has been selected to play 3 All-Star games.",
                        drafted='2021 Rnd 2, Pick 39 by DET',
                        position='Small Forward',
                        )

        player29 = Player(name="Giannis Antetokounmpo",
                        height="6'11",
                        weight="243", 
                        team=team6.id,
                        number=34,
                        image="/assets/players/ant.avif",
                        birthday='Decemeber 6, 1994 (29)',
                        bio="From Greece, Giannis has averaged 23.4 points, 4.9 assists, and 9.8 rebounds in 792 regular-season games. Giannis has played 11 seasons for the Bucks. He has been selected to play 7 All-Star games.",
                        drafted='2013 Rnd 1, Pick 15 by MIL',
                        position='Power Forward',
                        )
        
        player30 = Player(name="Brook Lopez",
                        height="7'1",
                        weight="282", 
                        team=team6.id,
                        number=11,
                        image="/assets/players/brook.png",
                        birthday='April 1, 1988 (36)',
                        bio="From North Hollywood, Brook Lopez has averaged 16.1 points and 6.2 rebounds in 1,025 regular-season games. Lopez has played 16 seasons for the Bucks, Nets, and Bulls. He has been selected to play in 1 All-Star game.",
                        drafted='2008 Rnd 1, Pick 10 by NJN',
                        position='Center',
                        )
        

        
        db.session.add_all([player1, player2, player3, player4, player5, player6, player7, player8, player9, player10,
                             player11, player12, player13, player14, player15, player16, player17, player18, player19, player20,
                               player21, player22, player23, player24, player25, player26, player27, player28, player29, player30])
        db.session.commit() 



        # Lakers
        player_stats1 = PlayerStats(
                                    gp=71,
                                    minpg=35.3,
                                    rebpg=7.3,
                                    ppg=25.7,
                                    apg=8.3,
                                    spg=1.3,
                                    bpg=0.5,
                                    tpg=3.5,
                                    fgpercentage=54.0,
                                    threepercentage=41.0,
                                    player_id=1
                                    )
        
        player_stats2 = PlayerStats(
                                    gp=76,
                                    minpg=32.7,
                                    rebpg=3.1,
                                    ppg=18.0,
                                    apg=6.3,
                                    spg=0.9,
                                    bpg=0.5,
                                    tpg=2.1,
                                    fgpercentage=45.6,
                                    threepercentage=82.8,
                                    player_id=2
                                    )
        
        player_stats3 = PlayerStats(
                                    gp=76,
                                    minpg=35.5,
                                    rebpg=12.6,
                                    ppg=24.7,
                                    apg=3.5,
                                    spg=1.2,
                                    bpg=2.3,
                                    tpg=2.1,
                                    fgpercentage=55.6,
                                    threepercentage=27.1,
                                    player_id=3
                                    )
        
        player_stats4 = PlayerStats(
                                    gp=82,
                                    minpg=32.1,
                                    rebpg=4.3,
                                    ppg=15.9,
                                    apg=5.5,
                                    spg=0.8,
                                    bpg=0.3,
                                    tpg=2.1,
                                    fgpercentage=48.6,
                                    threepercentage=36.7,
                                    player_id=4
                                    )
        
        player_stats5 = PlayerStats(
                                    gp=78,
                                    minpg=27.0,
                                    rebpg=2.9,
                                    ppg=8.9,
                                    apg=1.5,
                                    spg=0.7,
                                    bpg=0.4,
                                    tpg=0.9,
                                    fgpercentage=44.2,
                                    threepercentage=39.9,
                                    player_id=5
                                    )
        
        
        # Warriors
        player_stats6 = PlayerStats(
                                    gp=74,
                                    minpg=32.7,
                                    rebpg=4.5,
                                    ppg=26.4,
                                    apg=5.1,
                                    spg=0.7,
                                    bpg=0.4,
                                    tpg=2.8,
                                    fgpercentage=45.0,
                                    threepercentage=40.8,
                                    player_id=6
                                    )
        
        player_stats7 = PlayerStats(
                                    gp=77,
                                    minpg=29.7,
                                    rebpg=3.3,
                                    ppg=17.9,
                                    apg=2.3,
                                    spg=0.6,
                                    bpg=0.5,
                                    tpg=1.5,
                                    fgpercentage=43.2,
                                    threepercentage=38.7,
                                    player_id=7
                                    )
        
        player_stats8 = PlayerStats(
                                    gp=71,
                                    minpg=27.0,
                                    rebpg=4.5,
                                    ppg=13.2,
                                    apg=1.7,
                                    spg=0.6,
                                    bpg=0.6,
                                    tpg=1.2,
                                    fgpercentage=45.3,
                                    threepercentage=35.8,
                                    player_id=8
                                    )
        
        player_stats9 = PlayerStats(
                                    gp=55,
                                    minpg=27.1,
                                    rebpg=7.2,
                                    ppg=8.6,
                                    apg=6.0,
                                    spg=1.0,
                                    bpg=0.9,
                                    tpg=2.5,
                                    fgpercentage=49.7,
                                    threepercentage=39.5,
                                    player_id=9
                                    )
        
        player_stats10 = PlayerStats(
                                    gp=74,
                                    minpg=16.1,
                                    rebpg=5.7,
                                    ppg=4.5,
                                    apg=1.8,
                                    spg=0.4,
                                    bpg=0.4,
                                    tpg=0.7,
                                    fgpercentage=59.7,
                                    threepercentage=0.0,
                                    player_id=10
                                    )
        
        # Celtics
        player_stats11 = PlayerStats(
                                    gp=69,
                                    minpg=32.8,
                                    rebpg=5.4,
                                    ppg=12.5,
                                    apg=4.8,
                                    spg=0.9,
                                    bpg=0.8,
                                    tpg=1.8,
                                    fgpercentage=48.0,
                                    threepercentage=42.9,
                                    player_id=11
                                    )
        
        player_stats12 = PlayerStats(
                                    gp=73,
                                    minpg=32.6,
                                    rebpg=4.2,
                                    ppg=15.2,
                                    apg=5.2,
                                    spg=1.0,
                                    bpg=1.2,
                                    tpg=1.5,
                                    fgpercentage=46.1,
                                    threepercentage=39.6,
                                    player_id=12
                                    )
        
        player_stats13 = PlayerStats(
                                    gp=70,
                                    minpg=33.5,
                                    rebpg=5.5,
                                    ppg=23.0,
                                    apg=3.6,
                                    spg=1.2,
                                    bpg=0.5,
                                    tpg=2.4,
                                    fgpercentage=49.9,
                                    threepercentage=35.4,
                                    player_id=13
                                    )
        
        player_stats14 = PlayerStats(
                                    gp=74,
                                    minpg=35.7,
                                    rebpg=8.1,
                                    ppg=26.9,
                                    apg=4.9,
                                    spg=1.0,
                                    bpg=0.6,
                                    tpg=2.5,
                                    fgpercentage=47.1,
                                    threepercentage=37.6,
                                    player_id=14
                                    )
        
        player_stats15= PlayerStats(
                                    gp=57,
                                    minpg=29.6,
                                    rebpg=7.2,
                                    ppg=20.1,
                                    apg=2.0,
                                    spg=0.7,
                                    bpg=1.9,
                                    tpg=1.6,
                                    fgpercentage=51.6,
                                    threepercentage=37.5,
                                    player_id=15
                                    )
        
        # Cavs
        player_stats16 = PlayerStats(
                                    gp=57,
                                    minpg=33.4,
                                    rebpg=2.7,
                                    ppg=18.0,
                                    apg=6.6,
                                    spg=1.3,
                                    bpg=0.1,
                                    tpg=3.1,
                                    fgpercentage=44.6,
                                    threepercentage=37.1,
                                    player_id=16
                                    )
        
        player_stats17 = PlayerStats(
                                    gp=55,
                                    minpg=35.3,
                                    rebpg=5.1,
                                    ppg=26.2,
                                    apg=6.1,
                                    spg=1.8,
                                    bpg=0.5,
                                    tpg=2.8,
                                    fgpercentage=46.2,
                                    threepercentage=36.8,
                                    player_id=17
                                    )
        
        player_stats18 = PlayerStats(
                                    gp=68,
                                    minpg=28.8,
                                    rebpg=4.1,
                                    ppg=14.0,
                                    apg=5.1,
                                    spg=1.1,
                                    bpg=0.5,
                                    tpg=1.7,
                                    fgpercentage=42.1,
                                    threepercentage=32.5,
                                    player_id=18
                                    )
        
        player_stats19 = PlayerStats(
                                    gp=50,
                                    minpg=30.6,
                                    rebpg=9.4,
                                    ppg=15.7,
                                    apg=3.2,
                                    spg=0.9,
                                    bpg=1.4,
                                    tpg=1.8,
                                    fgpercentage=58.0,
                                    threepercentage=37.3,
                                    player_id=19
                                    )
        
        player_stats20 = PlayerStats(
                                    gp=77,
                                    minpg=31.7,
                                    rebpg=10.5,
                                    ppg=16.5,
                                    apg=2.7,
                                    spg=0.7,
                                    bpg=1.1,
                                    tpg=1.6,
                                    fgpercentage=63.4,
                                    threepercentage=0.0,
                                    player_id=20
                                    )
        
        # Magic
        player_stats21 = PlayerStats(
                                    gp=81,
                                    minpg=22.4,
                                    rebpg=3.8,
                                    ppg=11.6,
                                    apg=2.9,
                                    spg=0.8,
                                    bpg=0.5,
                                    tpg=1.6,
                                    fgpercentage=43.5,
                                    threepercentage=33.8,
                                    player_id=21
                                    )
        
        player_stats22 = PlayerStats(
                                   gp=75,
                                    minpg=27.0,
                                    rebpg=3.1,
                                    ppg=12.6,
                                    apg=2.7,
                                    spg=1.4,
                                    bpg=0.6,
                                    tpg=1.8,
                                    fgpercentage=47.1,
                                    threepercentage=39.7,
                                    player_id=22
                                    )
        
        player_stats23 = PlayerStats(
                                    gp=72,
                                    minpg=32.5,
                                    rebpg=5.3,
                                    ppg=19.7,
                                    apg=3.7,
                                    spg=1.1,
                                    bpg=0.4,
                                    tpg=1.9,
                                    fgpercentage=48.2,
                                    threepercentage=28.1,
                                    player_id=23
                                    )
        
        player_stats24 = PlayerStats(
                                    gp=80,
                                    minpg=35.0,
                                    rebpg=6.9,
                                    ppg=22.6,
                                    apg=5.4,
                                    spg=0.9,
                                    bpg=0.6,
                                    tpg=3.1,
                                    fgpercentage=45.5,
                                    threepercentage=33.9,
                                    player_id=24
                                    )
        
        player_stats25 = PlayerStats(
                                    gp=55,
                                    minpg=25.6,
                                    rebpg=6.9,
                                    ppg=11.0,
                                    apg=1.7,
                                    spg=0.6,
                                    bpg=0.5,
                                    tpg=1.2,
                                    fgpercentage=52.5,
                                    threepercentage=37.4,
                                    player_id=25
                                    )
        


        # Bucks

        player_stats26 = PlayerStats(
                                    gp=73,
                                    minpg=35.3,
                                    rebpg=4.4,
                                    ppg=24.3,
                                    apg=7.0,
                                    spg=1.0,
                                    bpg=0.2,
                                    tpg=2.6,
                                    fgpercentage=42.4,
                                    threepercentage=35.4,
                                    player_id=26
                                    )
        
        player_stats27 = PlayerStats(
                                   gp=79,
                                    minpg=29.6,
                                    rebpg=3.7,
                                    ppg=11.3,
                                    apg=1.4,
                                    spg=0.7,
                                    bpg=0.1,
                                    tpg=0.7,
                                    fgpercentage=44.3,
                                    threepercentage=41.3,
                                    player_id=27
                                    )
        
        player_stats28 = PlayerStats(
                                    gp=55,
                                    minpg=27.0,
                                    rebpg=4.7,
                                    ppg=15.1,
                                    apg=5.3,
                                    spg=0.9,
                                    bpg=0.3,
                                    tpg=2.3,
                                    fgpercentage=49.3,
                                    threepercentage=38.1,
                                    player_id=28
                                    )
        
        player_stats29 = PlayerStats(
                                    gp=73,
                                    minpg=35.2,
                                    rebpg=11.5,
                                    ppg=30.4,
                                    apg=6.5,
                                    spg=1.2,
                                    bpg=1.1,
                                    tpg=3.4,
                                    fgpercentage=61.1,
                                    threepercentage=27.4,
                                    player_id=29
                                    )
        
        player_stats30 = PlayerStats(
                                    gp=55,
                                    minpg=25.6,
                                    rebpg=6.9,
                                    ppg=11.0,
                                    apg=1.7,
                                    spg=0.6,
                                    bpg=0.5,
                                    tpg=1.2,
                                    fgpercentage=52.5,
                                    threepercentage=37.4,
                                    player_id=30
                                    )


        
        db.session.add_all([player_stats1, player_stats2, player_stats3, player_stats4, player_stats5, player_stats6, player_stats7, player_stats8, player_stats9, player_stats10,
                             player_stats11, player_stats12, player_stats13, player_stats14, player_stats15, player_stats16, player_stats17, player_stats18, player_stats19, player_stats20, 
                             player_stats21, player_stats22, player_stats23, player_stats24, player_stats25, player_stats26, player_stats27, player_stats28, player_stats29, player_stats30])
        db.session.commit()


        # Lakers
        team_players1 = PlayerTeam(player_id=1,
                                   team_id=1,
                                   role="Small Forward"
                            
        )
        team_players2 = PlayerTeam(player_id=2,
                                   team_id=1,
                                   role="Point Guard"
                            
        )
        team_players3 = PlayerTeam(player_id=3,
                                   team_id=1,
                                   role="Power Forward"
                            
        )
        team_players4 = PlayerTeam(player_id=4,
                                   team_id=1,
                                   role="Shooting Guard"
                            
        )
        team_players5 = PlayerTeam(player_id=5,
                                   team_id=1,
                                   role="Power Forward"
                            
        )



        # Warriors
        team_players6 = PlayerTeam(player_id=6,
                                   team_id=2,
                                   role="Point Guard"
                            
        )
        team_players7 = PlayerTeam(player_id=7,
                                   team_id=2,
                                   role="Shooting Guard"
                            
        )
        team_players8 = PlayerTeam(player_id=8,
                                   team_id=2,
                                   role="Small Forward"
                            
        )
        team_players9 = PlayerTeam(player_id=9,
                                   team_id=2,
                                   role="Power Forward"
                            
        )
        team_players10 = PlayerTeam(player_id=10,
                                   team_id=2,
                                   role="Power Forward"
                            
        )

        # Celtics
        team_players11 = PlayerTeam(player_id=11,
                                   team_id=3,
                                   role="Point Guard"
                            
        )
        team_players12 = PlayerTeam(player_id=12,
                                   team_id=3,
                                   role="Shooting Guard"
                            
        )
        team_players13 = PlayerTeam(player_id=13,
                                   team_id=3,
                                   role="Small Forward"
                            
        )
        team_players14 = PlayerTeam(player_id=14,
                                   team_id=3,
                                   role="Small Forward"
                            
        )
        team_players15 = PlayerTeam(player_id=15,
                                   team_id=3,
                                   role="Power Forward"
                            
        )

        # Cavs
        team_players16 = PlayerTeam(player_id=16,
                                   team_id=4,
                                   role="Point Guard"
                            
        )
        team_players17 = PlayerTeam(player_id=17,
                                   team_id=4,
                                   role="Shooting Guard"
                            
        )
        team_players18 = PlayerTeam(player_id=18,
                                   team_id=4,
                                   role="Small Forward"
                            
        )
        team_players19 = PlayerTeam(player_id=19,
                                   team_id=4,
                                   role="Power Forward"
                            
        )
        team_players20 = PlayerTeam(player_id=20,
                                   team_id=4,
                                   role="Center"
                            
        )

        # Magic
        team_players21 = PlayerTeam(player_id=21,
                                   team_id=5,
                                   role="Point Guard"
                            
        )
        team_players22 = PlayerTeam(player_id=22,
                                   team_id=5,
                                   role="Shooting Guard"
                            
        )
        team_players23 = PlayerTeam(player_id=23,
                                   team_id=5,
                                   role="Small Forward"
                            
        )
        team_players24 = PlayerTeam(player_id=24,
                                   team_id=5,
                                   role="Power Forward"
                            
        )
        team_players25 = PlayerTeam(player_id=25,
                                   team_id=5,
                                   role="Center"
                            
        )

        # Bucks
        team_players26 = PlayerTeam(player_id=26,
                                   team_id=6,
                                   role="Point Guard"
                            
        )
        team_players27 = PlayerTeam(player_id=27,
                                   team_id=6,
                                   role="Shooting Guard"
                            
        )
        team_players28 = PlayerTeam(player_id=28,
                                   team_id=6,
                                   role="Small Forward"
                            
        )
        team_players29 = PlayerTeam(player_id=29,
                                   team_id=6,
                                   role="Power Forward"
                            
        )
        team_players30 = PlayerTeam(player_id=30,
                                   team_id=6,
                                   role="Center"
                            
        )


        db.session.add_all([team_players1, team_players2, team_players3, team_players4, team_players5, team_players6, team_players7, team_players8, team_players9, team_players10, 
                            team_players11, team_players12, team_players13, team_players14, team_players15, team_players16, team_players17, team_players18, team_players19, team_players20, 
                            team_players21, team_players22, team_players23, team_players24, team_players25, team_players26, team_players27, team_players28, team_players29, team_players30])
        db.session.commit()
        

        # Seed code goes here! 
        print("Completed seeding!")

