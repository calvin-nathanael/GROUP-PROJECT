from pathlib import Path
import csv

def profitloss_function(forex):

    pl_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"

    report_path = Path.cwd()/"summary_report.txt"

    # opening the file
    with pl_path.open(mode="r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)

        # appending all days and net profits to the lists
        pl_list = []
        for line in reader:
            pl_list.append(line)

        # creating empty variables
        index = 0
        deficit = 0
        
        # using while loop, to go through all the days in the list
        while index + 1 < len(pl_list):
            
            # using if function to check if the previous day is more than the current
            if float(pl_list[index][4]) > float(pl_list[index + 1][4]):

                # calculating the deficit, and assigning it to the deficit variable
                deficit = float(pl_list[index][4]) - float(pl_list[index + 1][4])

                # writing the appropriate CASH DEFICIT line into the summary report, converting the amount to SGD using forex.
                with report_path.open(mode="a") as file:
                    file.write(f"\n[PROFIT DEFICIT] DAY: {pl_list[index+1][0]}, AMOUNT: SGD{round((deficit * forex),2)}")
                    file.close()
            
            # adding 1 to index before it loops
            index += 1

        # initially, deficit variable was assigned as 0. if there are no deficits, the code above will not assigned anything to the deficit variable.
        # using if function to check if the deficit variable remained at 0
        if deficit == 0:

            # writing cash surplus line into the summary report
            with report_path.open(mode="a") as file:
                file.write("\n[PROFIT SURPLUS] Net profit on each period is higher than the previous period")
                file.close()

        file.close()
