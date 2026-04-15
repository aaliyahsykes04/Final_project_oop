# This is the math class 
# takes clean list of Records and computers metrics to test our thesis 

from domain.analysis_result import AnalysisResult

class Analyzer:
    def __init__(self, records):
        #records = the clean list of Record objects from the Normalizer 
        self.records = records

    def analyze(self):
        # will group records by team and compute stats for each team 
        # going to be using dictionary 
        team_stats = {}

        for record in self.records:
            team = record.team 

            # if i havent seen this team pop up yet, set up empty stats from team 
            if team not in team_stats:
                team_stats[team] = {'wins': 0, 'losses': 0, 'total_rush':0 , 'games':0}

            # add this game's data to the team's running totals
            team_stats[team]['games'] += 1
            team_stats[team]['total_rush'] += record.rush_attempts
            if record.result == 'W':
                team_stats[team]['wins'] += 1
            else: 
                team_stats[team]['losses'] += 1 

        #now computing averages for each team 
        # avg_rush_wins = average rush attempts in games they won 
        win_rushes = [r.rush_attempts for r in self.records if r.result == 'W']
        loss_rushes =[r.rush_attempts for r in self.records if r.result == 'L']

        #Calculate the overall averages 
        avg_rush_wins = sum(win_rushes) / len(win_rushes) if win_rushes else 0 
        avg_rush_losses = sum(loss_rushes) / len(loss_rushes) if loss_rushes else 0

        #write the conclusion based on what the numbers show 
        if avg_rush_wins > avg_rush_losses:
                conclusion = (
                    f"SUPPORTED — Teams averaged {avg_rush_wins:.1f} rush attempts in wins "
                    f"vs {avg_rush_losses:.1f} in losses."
                )
        else:
            conclusion = (
            f"NOT SUPPORTED — Teams averaged {avg_rush_wins:.1f} rush attempts in wins "
            f"vs {avg_rush_losses:.1f} in losses."
            )

        # Build grouped data by team for the results table
        grouped = {}
        for team, stats in team_stats.items():
            games = stats['games']
            grouped[team] = {
                'wins': stats['wins'],
                'losses': stats['losses'],
                'win_rate': round(stats['wins'] / games, 3) if games else 0,
                'avg_rush': round(stats['total_rush'] / games, 1) if games else 0
            }


        # Return an AnalysisResult object with everything packed in
        return AnalysisResult(
            metric_name="Average Rush Attempts: Wins vs Losses",
            value=round(avg_rush_wins, 2),
            grouped_data=grouped,
            conclusion=conclusion
        )