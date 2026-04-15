# NFL Rush Attempt Thesis Analyzer

## Thesis
NFL teams that run the ball more often win more games.

## Data Source
- Library: `nfl_data_py`
- Data: Play-by-play data from the nflverse project
- Seasons: 2021, 2022, 2023
- Link: https://github.com/nflverse/nflverse-data

## How to Run
1. Make sure Python 3.11 is installed
2. Install the required library:
py -3.11 -m pip install nfl_data_py
3. 3. Run the program:
py -3.11 main.py


## Data Structures Used

### Dictionary (HashMap)
- Used in `Repository` to group records by team
- Used in `Analyzer` to accumulate stats per team
- Why: Looking up a team by name is O(1) — instant regardless of how many teams there are

### List
- Used in `Normalizer` to store cleaned records
- Used in `Analyzer` to collect rush attempts for wins and losses
- Why: Good for sequential processing with map/filter. Iteration is O(n)

## Big O Notes
| Operation | Structure | Big O |
|---|---|---|
| Look up a team | Dictionary | O(1) |
| Loop through all records | List | O(n) |
| Group plays by game | Pandas groupby | O(n log n) |
| Sort teams by win rate | List sort | O(n log n) |

## Findings
- Total game records analyzed: 1708
- Average rush attempts in wins: 30.9
- Average rush attempts in losses: 23.5
- Conclusion: **SUPPORTED** — teams that ran the ball more won more games

### Top 10 Teams by Win Rate (2021-2023)
| Team | Wins | Losses | Win Rate | Avg Rush |
|---|---|---|---|---|
| KC | 42 | 19 | 0.689 | 25.2 |
| PHI | 36 | 20 | 0.643 | 31.5 |
| BUF | 36 | 20 | 0.643 | 28.2 |
| DAL | 35 | 20 | 0.636 | 28.8 |
| SF | 37 | 23 | 0.617 | 29.4 |
| CIN | 33 | 24 | 0.579 | 24.2 |
| BAL | 31 | 23 | 0.574 | 31.1 |
| MIA | 29 | 24 | 0.547 | 25.0 |
| GB | 29 | 25 | 0.537 | 26.4 |
| LA | 29 | 27 | 0.518 | 25.8 |