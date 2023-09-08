import csv

def main():
    # Initialize variables for PyBank calculations
    total_months = 0
    total_profit_losses = 0
    previous_profit_losses = None
    profit_losses_changes = []
    greatest_increase = {"Date": None, "Amount": float("-inf")}  # Initialize with negative infinity
    greatest_decrease = {"Date": None, "Amount": float("inf")}  # Initialize with positive infinity

    # Read the budget_data.csv file and perform calculations
    with open('/Users/hprincivil/Documents/GitHub/python-challenge/PyBank/budget_data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header row

        for row in csvreader:
            date, profit_losses = row
            profit_losses = int(profit_losses)
            
            # Calculate total number of months
            total_months += 1
            
            # Calculate net total amount of "Profit/Losses"
            total_profit_losses += profit_losses
            
            # Calculate changes in "Profit/Losses"
            if previous_profit_losses is not None:
                change = profit_losses - previous_profit_losses
                profit_losses_changes.append(change)
                
                # Check for greatest increase in profits
                if change > greatest_increase["Amount"]:
                    greatest_increase = {"Date": date, "Amount": change}
                
                # Check for greatest decrease in profits
                if change < greatest_decrease["Amount"]:
                    greatest_decrease = {"Date": date, "Amount": change}
            
            # Update the previous_profit_losses for the next iteration
            previous_profit_losses = profit_losses

    # Calculate average change in "Profit/Losses"
    average_change = sum(profit_losses_changes) / len(profit_losses_changes)

    # Function to write and print analysis
    def write_and_print_pybank_analysis(file_path):
        with open(file_path, 'w') as file:
            lines = [
                "Financial Analysis",
                "----------------------------",
                f"Total Months: {total_months}",
                f"Total: ${total_profit_losses}",
                f"Average Change: ${average_change:.2f}",
                f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})",
                f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})"
            ]
            for line in lines:
                print(line)
                file.write(line + "\n")

    # Specify the output file path for PyBank analysis
    pybank_output_file_path = '/Users/hprincivil/Documents/GitHub/python-challenge/PyBank/pybank_analysis.txt'

    # Write the analysis to a text file and print to terminal
    write_and_print_pybank_analysis(pybank_output_file_path)

if __name__ == '__main__':
    main()
