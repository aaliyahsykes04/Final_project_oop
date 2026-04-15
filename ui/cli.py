# this is the UI - what the user will actually sees and interacts with
# ties all the other classes together and prints the results

from persistence.api_client import ApiClient
from persistence.repository import Repository
from services.normalizer import Normalizer
from services.analyzer import Analyzer
from domain.thesis import Thesis

def run():
    #print the welcome message 
    print("=" * 60)
    print("NFL Rush Attempt Thesis Analyzer")
    print("=" * 60)

    #creat the thesis object - stores what we are trying to prove 
    thesis = Thesis(
        statement="NFL teams that run the ball more often win more games.",
        independent_var="Rush Attempts",
        dependent_var="Win/Loss Result",
        filter_note="Regular season only, 2021-2023"
    )
    print(f"\n{thesis}\n")

    #Step1 : Fetch the data from the API 
    client = ApiClient(seasons=[2021, 2022, 2023])
    raw_data = client.fetch_games()

    # Step 2 — Load it into the repository and convert to Record objects
    repo = Repository()
    repo.load(raw_data)

    # Step 3 — Clean the data
    normalizer = Normalizer(repo.get_all_records())
    clean_records = normalizer.clean()

    # Step 4 — Run the analysis
    analyzer = Analyzer(clean_records)
    result = analyzer.analyze()

    # Step 5 — Print the results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(result)

    # Print a small table of top 10 teams by win rate
    print("\nTop 10 Teams by Win Rate:")
    print(f"{'Team':<30} {'Wins':<6} {'Losses':<8} {'Win Rate':<10} {'Avg Rush'}")
    print("-" * 65)

    # Sort teams by win rate — highest first
    sorted_teams = sorted(result.grouped_data.items(), key=lambda x: x[1]['win_rate'], reverse=True)

    for team, stats in sorted_teams[:10]:
        print(f"{team:<30} {stats['wins']:<6} {stats['losses']:<8} {stats['win_rate']:<10} {stats['avg_rush']}")

if __name__ == "__main__":
    run()
