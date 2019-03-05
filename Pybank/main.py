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


def convert_prof_loss(all_data):
    #convert prof loss to integer
    new_data = []
    for row in all_data:
        new_row = []
        new_row.append(row[0])
        new_row.append(int(row[1]))
        new_data.append(new_row)
    return new_data


def determine_total_months(data):
    num_months = len(data)
    return num_months


def compute_net_profit_loss(data):
    net_prof_loss = 0
    for row in data:
        prof_loss = row[1]
        net_prof_loss += prof_loss
    return net_prof_loss


def compute_all_changes(data):
    change = []
    last_month_value = data[0][1]
    for row in data[1:]:
        difference = row[1] - last_month_value
        change.append([row[0], difference])
        last_month_value = row[1]
    return change


def compute_average_change(data):
    change_total = 0
    for row in data:
        change_total += row[1]
    average_change = change_total / len(data)
    return average_change


def determine_max_increase_decrease(data, min_or_max):
    #using min or max, get the max increase and decrease in profit and loss
    change_list = []
    for row in data:
        change_list.append(row[1])
    value = min_or_max(change_list)
    value_month = data[change_list.index(value)][0]
    return value_month, value


pybank_path = os.path.join(".", 'Resources', "budget_data.csv")

header, pybank_data_raw = open_csv_data(pybank_path)

pybank_data = convert_prof_loss(pybank_data_raw)

total_months = determine_total_months(pybank_data)

net_profit_loss = compute_net_profit_loss(pybank_data)

prof_loss_change = compute_all_changes(pybank_data)

average_change = round(compute_average_change(prof_loss_change),2)

max_increase_month, max_increase = determine_max_increase_decrease(prof_loss_change, max)

max_decrease_month, max_decrease = determine_max_increase_decrease(prof_loss_change, min)

#print summary

print('Financial Analysis')
print('-' * 20)
print(f'Total Months: {total_months}')
print(f'Total: ${net_profit_loss}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})')

    
create_txt = open("Pybank_Analysis.txt", "w+")
    
create_txt.write('Financial Analysis' + '\n')
create_txt.write('-' * 20 + '\n')
create_txt.write(f'Total Months: {total_months}' + '\n')
create_txt.write(f'Total: ${net_profit_loss}' + '\n')
create_txt.write(f'Average Change: ${round(average_change, 2)} \n')
create_txt.write(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})' + '\n')
create_txt.write(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})' + '\n')
    
create_txt.close()