import os
import csv
budget_csv = os.path.join('..','Resources', 'budget_data.csv')
budget_txt_file = os.path.join("budget_txt_file.txt")

months_change = []
net_change_list = []
increasevar= ["", 0]
decreasevar = ["", 9999999999999999999]
total_months= 0
total_net = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row=next(csvreader)

    for row in csvreader:
        total_months += 1
        total_net += int(first_row[1])
        net_change_list += [total_net]
        months_change += [row[0]]

        if total_net > increasevar[1]:
            increasevar[0] = row[0]
            increasevar[1] = total_net

        if total_net < decreasevar[1]:
            decreasevar[0] = row[0]
            decreasevar[1] = total_net

net_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"Financial Analysis"
    f"-------------------------------"
    f"Total Months: {total_months}"
    f"Total: ${total_net}"
    f"Average Change: ${net_avg: .2f}"
    f"Greatest Increase in Profits: {increasevar[0]} (${increasevar[1]})"
    f"Greatest Decrease in Profits: {decreasevar[0]} (${decreasevar[1]})")

with open(budget_txt_file, "w") as txt_file:
    txt_file.write(output)
