# this class takes raw data from ApiClient and stores it in memory and converts raw rows into Record

from domain.record import Record

class Repository : 
    def __init__(self):
        #This dictionary will store out record grouped by team 
        # allows the look team instantly 
        self.records_by_team = {}

    def load (self, raw_df):
        #raw_df is the big spreadsheet from ApiClient 
        # need it to be turned into individual Record objects 

        #first - group all the plays by game so its one row per game 
        # groupby - group all plays that share the same game_id, team, week, season 
        grouped = raw_df.groupby(['game_id', 'posteam', 'week', 'season'])

        for (game_id, team, week, season), group in grouped:
            #count total rush attempts for this team in this game 
            rush_attempts = int(group['rush_attempt'].sum())

            #Figure out if they won - compare final scores 
            final_team_score = group['posteam_score'].max()
            final_oop_score = group['defteam_score'].max()
            result = "W" if final_team_score > final_oop_score else "L"

            # create one records for this game 
            record = Record(team, week, season, rush_attempts, result)

            #Add it to the dictionary under the team name 
            if team not in self.records_by_team:
                self.records_by_team[team] = []
            self.records_by_team[team].append(record)

        print(f"Loaded {sum(len(v) for v in self.records_by_team.values())} game records.")

    def get_all_records (self):
        #returns every single record as on flat list
        # use a list comprehension here - clean python loop and build a list 
        return [record for records in self.records_by_team.values() for record in records]