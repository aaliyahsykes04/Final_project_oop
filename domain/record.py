# this class will represent 1 game for 1 team. 
# every game pulled from the API will become one record object.

class Record: 
    def __init__(self, team, week, season, rush_attempts, result):
        # __init__ runs automatically when you create a new Record 
        # fills out a form for one game 

        self.team = team   # team name ex. THE PHILADELPHIS EAGLES GO BIRDS 
        self.week = week  # which week of the season the game is
        self.season = season  # the year of the game 
        self.rush_attempts = rush_attempts  # how many times they ran the ball 
        self.result = result # did they win or lose? 

    def __repr__(self):
        # __repr__ controls what prints when you do print(record)
    
        return f"Record ({self.team} , Week {self.week}, {self.results}, {self.rush_attempts} rushes)"
        # returns the statement with the info filled out 

        
    
