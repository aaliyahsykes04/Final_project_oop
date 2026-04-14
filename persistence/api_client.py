# this class is responsible for fetching raw data from internet
# grab NFL game data


import nfl_data_py as nfl 

class ApiClient: 
    def __init__(self, seasons):
        # seasons - list of years i want from the nfl data 
        self.seasons = seasons

    def fetch_games(self):
        # this calls the nfl data library and pulls play by play data 
        # it returns a pandas Dataframe 
        print (f"Fetching NFL data for seasons: {self.seasons}...")

        #pbp = play by play. Every play from every game
        pbp = nfl.import_pbp_data(self.seasons)

        #  only keep columns i actually need 
        # each row is one play from one game
        columns = ['posteam', 'week', 'season','rush_attempt', 'posteam_score','defteam_score','game_id']
        pbp_filtered =pbp[columns]

        print(f"Pulled {len(pbp_filtered)} rows of data.")
        return pbp_filtered