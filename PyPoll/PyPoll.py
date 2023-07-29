import os
import csv
election_csv = os.path.join('..','Resources', 'election_data.csv')
election_txt_file = os.path.join("election_txt_file.txt")

candidate_option = []
candidate_votes = {}
winner = [""]
win_count = 0
total_votes = 0

with open (election_csv) as election_data:
    csvreader = csv.reader(election_data)
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[1]

        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open (election_txt_file, "w") as txt_file:
    election_results = (
        f"Election Results"
        f"---------------------"
        f"Total Votes: {total_votes}"
        f"---------------------")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > win_count):
            win_count = votes
            winner = candidate

        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})"
        print(voter_output, end="")

        txt_file.write(voter_output)

    winner_summary = (
        f"--------------------"
        f"Winner: {winner}"
        f"--------------------")
    print(winner_summary)

    txt_file.write(winner_summary)
