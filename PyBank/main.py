import os
import csv

# Set Path For File
csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables
months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0


# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first 
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Set variables for rows and calculate months and net amount 
    months += 1
    net_amount += int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]
    
    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate months
        months += 1
        # Calculate Net Amount 
        net_amount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]  
        
    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"")
print(f"---------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits:, {greatest_inc_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_dec_month}, (${lowest})")

# Specify File To Write To
#csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

	# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file,'w',) as txtfile:
	
# Write New Data
    txtfile.write(f"Financial Analysis")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {months}")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_inc_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_dec_month}, (${lowest})\n")
    



