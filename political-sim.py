import random

class Person:
    economic_leaning = 0
    social_leaning = 0

class Candidate (Person): # Barely
    name = ""
    trustworthiness = 0
    likeability = 0

    def make_statement (self):
        print ("Hello, I am", self.name)
        print ("I'm not biased, and I'm 100% trustworthy!")


    def __init__ (self, nm, ec, sc, tr, lk):
        self.name = nm
        self.economic_leaning = ec
        self.social_leaning = sc
        self.trustworthiness = tr - 0.3
        self.likeability = tr - 0.4

    def lost_election (self):
        if (self.likeability >= 0.6):
            print ("Fair enough, I hope they do well in office.")
        else:
            print ("NOOOO they STOLE the Election! this should be rightfully MINE, but the EVIL Opposition are committing FRAUD!")

class Voter (Person):
    gullibility = 0
    economic_leaning = 0
    social_leaning = 0

    def vote (self, *candidates):
        vote_ratings = []
        for candidate in candidates:
            economic_rating = 2 - abs (self.economic_leaning - candidate.economic_leaning)
            social_rating = 2 - abs (self.social_leaning - candidate.social_leaning)
            rating = economic_rating + social_rating #+ ((candidate.trustworthiness*(self.gullibility+1))/2) + ((candidate.likeability*(self.gullibility+1))/2)
            vote_ratings.append (rating)

        i = 0
        m = 0
        for r in range (0, len(vote_ratings)):
            if vote_ratings[r] > m:
                m = vote_ratings[r]
                i = r


        #print ("I'm voting for", candidates[i].name, "because I think they're great (score:", m, ").")
        return i

    def __repr__ (self):
        return f'Voter("{self.gullibility}", "{self.economic_leaning}", "{self.social_leaning}")'


    def __iadd__ (self, other):
        self.gullibility = (self.gulliblity + other.gullibility)/2
        self.economic_leaning = (self.economic_leaning + other.economic_leaning)/2
        self.social_leaning = (self.social_leaning + other.social_leaning)/2



trump = Candidate ("The Annoying Orange", 0.9, 0.9, -0.2, -0.3)
biden = Candidate ("Sleepy Joe", 0.8, 0.7, 0.3, 0.6)

trump.make_statement()
biden.make_statement()

tr = 0
bi = 0

for i in range (1, 32800):
    v = Voter ()
    v.gullibility = random.random ()
    v.social_leaning = (2*random.random ())-1
    v.economic_leaning = (2*random.random ())-1

    if v.vote (trump, biden) == 0:
        tr = tr + 1
    else:
        bi = bi + 1


print (f'There were "{tr}" votes for Trump, and "{bi}" votes for Biden!')
if (tr > bi):
    print ("Trump wins!")
    biden.lost_election()
elif (tr < bi):
    print ("Biden wins!")
    trump.lost_election()
                
            
            
