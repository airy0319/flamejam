#
# This is a short script to kill all tables and fill them with new test data.
# It should be run from a virtualenv.
#

from flamejam import db
from flamejam.models import Announcement, User, Jam, Game, Rating, Comment, GameScreenshot, DevlogPost
from datetime import datetime, timedelta

# Kill everything and recreate tables
db.drop_all()
db.create_all()

# Make users
peter = User("peter", "lol", "roflomg-peter@mailinator.com")
paul = User("opatut", "lol", "opatutlol@aol.com", is_admin = True, is_verified = True)
per = User("per", "lol", "roflomg-per@mailinator.com", is_verified = True, receive_emails = False)
pablo = User("pablo", "lol", "roflomg-pablo@mailinator.com")
paddy = User("paddy", "lol", "roflomg-paddy@mailinator.com")

# Add users
db.session.add(peter)
db.session.add(paul)
db.session.add(per)
db.session.add(pablo)
db.session.add(paddy)

# Make jams
rgj1 = Jam("BaconGameJam 01", datetime.utcnow() - timedelta(days=30))
rgj2 = Jam("BaconGameJam 2", datetime.utcnow() - timedelta(days=2))
rgj3 = Jam("BaconGameJam 3", datetime.utcnow())
loljam = Jam("Test Jam", datetime.utcnow() - timedelta(days=3))
rgj4 = Jam("BaconGameJam 4", datetime.utcnow() + timedelta(days=14))

rgj1.theme = "Bacon"
rgj2.theme = "Zombies"
rgj3.theme = "Space"
loljam.theme = "Funny"
rgj4.theme = "HIDDEN, SHOULD NOT BE SHOWN"

# Add jams
db.session.add(rgj1)
db.session.add(rgj2)
db.session.add(rgj3)
db.session.add(loljam)
db.session.add(rgj4)

# make people participate
peter.joinJam(rgj1)
paul.joinJam(rgj1)
paddy.joinJam(rgj2)
peter.joinJam(rgj3)
paul.joinJam(rgj3)
per.joinJam(rgj3)
pablo.joinJam(rgj3)
paddy.joinJam(rgj3)
paddy.joinJam(rgj4)
paul.joinJam(rgj4)
paul.joinJam(loljam)
paddy.joinJam(loljam)
pablo.joinJam(loljam)

aTeam = paul.getTeam(rgj3)
aTeam.userJoin(pablo)

# Make devlog post

db.session.add(DevlogPost(aTeam, paul, "Sugar and spice",
"""... and everything nice.

---

    // our super duper mega fail program
    int main() {
        return 1;
    }

![Rainbow Dash is best Pony!](http://i.imgur.com/nnKnB.png)"""))

# Make games
best_game = Game(paddy.getTeam(rgj3), "Bessy the Best Game")
best_game.description = "Simply the best game"

space_game = Game(aTeam, "CloneStars - The war wars")
space_game.description = "A space shooter game."

clone = Game(peter.getTeam(rgj3), "Shooterz")
clone.description = "I got this idea while taking a dump."

test_game = Game(per.getTeam(rgj3), "RIP VIP")

# Add games
db.session.add(best_game)
db.session.add(space_game)
db.session.add(clone)
db.session.add(test_game)

# Add screenshots
s1 = GameScreenshot("http://2.bp.blogspot.com/_gx7OZdt7Uhs/SwwanX_-API/AAAAAAAADAM/vbZbIPERdhs/s1600/Star-Wars-Wallpaper-star-wars-6363340-1024-768.jpg", "Awesome cover art", space_game)
s2 = GameScreenshot("http://images.psxextreme.com/wallpapers/ps3/star_wars___battle_1182.jpg", "Sample vehicles", space_game)
s3 = GameScreenshot("http://sethspopcorn.com/wp-content/uploads/2010/10/CloneTrooper.jpg", "Character selection screen", space_game)

db.session.add(s1)
db.session.add(s2)
db.session.add(s3)

# Make ratings
rating1 = Rating(3, 5, 1, 7, 3, 1, 5, 2, "cool stuff", best_game, peter)
rating2 = Rating(10, 6, 1, 7, 6, 10, 10, 10, "adasdff", best_game, paul)
rating3 = Rating(3, 5, 1, 5, 2, 2, 10, 3, "cadkak", space_game, paul)
rating4 = Rating(9, 5, 6, 7, 3, 1, 1, 6, "fakpdak1", clone, paul)
rating5 = Rating(3, 5, 8, 5, 3, 6, 4, 1, "madkm1njn", clone, paddy)

# Add ratings
db.session.add(rating1)
db.session.add(rating2)
db.session.add(rating3)
db.session.add(rating4)
db.session.add(rating5)

# Make comments
comment1 = Comment("lol so bad", best_game, peter)
comment2 = Comment("the worst", best_game, paul)
comment3 = Comment("You don't provide a download for your game. Please add one via \"Add package\".", space_game, paul)
comment4 = Comment("I really *love* this game. It is just awesome.", space_game, paul)
comment5 = Comment("@paul Now you have a download", space_game, paddy)

# Add comments
db.session.add(comment1)
db.session.add(comment2)
db.session.add(comment3)
db.session.add(comment4)
db.session.add(comment5)

# Make announcements
ann1 = Announcement("New game jam now.")
ann2 = Announcement("Game jam is over.")
ann3 = Announcement("Voting is over.")
ann4 = Announcement("New game jam announced.")
ann5 = Announcement("Game jam started.")

# Add announcements

db.session.add(ann1)
db.session.add(ann2)
db.session.add(ann3)
db.session.add(ann4)
db.session.add(ann5)

# Commmit it all
db.session.commit()
