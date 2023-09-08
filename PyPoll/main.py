import csv

def main():
    # Initialize variables for PyPoll calculations
    total_votes = 0
    candidates_votes = {}
    winner = None
    max_votes = 0
    
    # Read the election_data.csv file and perform calculations
    with open('/Users/hprincivil/Documents/GitHub/python-challenge/PyPoll/election_data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header row

        for row in csvreader:
            voter_id, county, candidate = row
            
            # Calculate total number of votes
            total_votes += 1
            
            # Update candidates' vote counts
            if candidate in candidates_votes:
                candidates_votes[candidate] += 1
            else:
                candidates_votes[candidate] = 1

            # Determine the winner
            if candidates_votes[candidate] > max_votes:
                max_votes = candidates_votes[candidate]
                winner = candidate

    # Function to write and print analysis
    def write_and_print_pypoll_analysis(file_path):
        with open(file_path, 'w') as file:
            lines = [
                "Election Results",
                "-------------------------",
                f"Total Votes: {total_votes}",
                "-------------------------"
            ]
            for line in lines:
                print(line)
                file.write(line + "\n")
            
            for candidate, votes in candidates_votes.items():
                percentage = (votes / total_votes) * 100
                print(f"{candidate}: {percentage:.3f}% ({votes})")
                file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
            
            lines = [
                "-------------------------",
                f"Winner: {winner}",
                "-------------------------"
            ]
            for line in lines:
                print(line)
                file.write(line + "\n")

    # Specify the output file path for PyPoll analysis
    pypoll_output_file_path = '/Users/hprincivil/Documents/GitHub/python-challenge/PyPoll/election_analysis.txt'

    # Write the analysis to a text file and print to terminal
    write_and_print_pypoll_analysis(pypoll_output_file_path)

if __name__ == '__main__':
    main()
