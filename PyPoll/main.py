import os
import csv

def open_csv_data(file_path):
    my_data = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ',')
        csv_header = next(csv_reader)
        for row in csv_reader:
            my_data.append(row)
    return csv_header, my_data


def compute_candidate_votes(data):
    total_votes = 0
    candidate_votes = {}
    for candidate in data:
        candidate_name = candidate[2]
        if candidate_name in candidate_votes.keys():
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
        total_votes += 1
    return total_votes, candidate_votes


def compute_candidate_vote_percentage(candidate_dict, total_votes):
    candidate_count_percentage = {}
    for name in candidate_dict.keys():
        vote_count = candidate_dict[name]
        percentage_vote = round((vote_count / total_votes)*100, 2)
        candidate_count_percentage[name] = [vote_count, percentage_vote]
    return candidate_count_percentage


    
def determine_winner(candidate_data):
    highest_percentage = 0
    winner_name = None
    for candidate in candidate_data:
        candidate_percentage = candidate_data[candidate][1]
        candidate_name = candidate
        if candidate_percentage > highest_percentage:
            highest_percentage = candidate_percentage
            winner_name = candidate_name
    return highest_percentage, winner_name

   

pypoll_path = os.path.join('.', 'Resources', 'election_data.csv')

csv_header, pypoll_data = open_csv_data(pypoll_path)

total_votes, votes_per_candidate = compute_candidate_votes(pypoll_data)

candidate_count_percentage = compute_candidate_vote_percentage(votes_per_candidate, total_votes)

winner_percentage, winner_name = determine_winner(candidate_count_percentage)

print('Election Results')
print('-' * 20)
print(f'Total Votes: {total_votes}')
print('-' * 20)
for candidate in candidate_count_percentage:
        print(f'{candidate}: {candidate_count_percentage[candidate][1]}% ({candidate_count_percentage[candidate][0]})')
print('-' * 20)
print(f'Winner: {winner_name}')
print('-' * 20)

create_txt = open("Pypoll_Analysis.txt", "w+")

create_txt.write('Election Results' + '\n')
create_txt.write('-' * 20 + '\n')
create_txt.write(f'Total Votes: {total_votes}' + '\n')
create_txt.write('-' * 20 + '\n')
for candidate in candidate_count_percentage:
        create_txt.write(f'{candidate}: {candidate_count_percentage[candidate][1]}% ({candidate_count_percentage[candidate][0]})' + '\n')
create_txt.write('-' * 20 + '\n')
create_txt.write(f'Winner: {winner_name}' + '\n')
create_txt.write('-' * 20 + '\n')

create_txt.close()