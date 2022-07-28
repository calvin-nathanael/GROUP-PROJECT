from pathlib import Path
import csv

def overheads_function(forex):
    
    # creating paths
    oh_path = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
    report_path = Path.cwd()/"project_group"/"summary_report.txt"

    # opening the file
    with oh_path.open(mode="r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)

        # appending contents of the file to a list, and the overheads in the list
        list = []
        overheads_list = []
        for line in reader:
            list.append(line)
            overheads_list.append(float(line[1]))

        # using for loop and if function to match a overhead to the highest overhead
        for category, overheads in list:
            if float(overheads) == max(overheads_list):

                # extracting the overhead and corresponding category and writing it in the summary report, and converting the overhead to SGD using forex
                with report_path.open(mode="a") as file:
                    file.write(f"\n[HIGHEST OVERHEADS] {category}: SGD{round((float(overheads)*forex),2)}")
                    file.close()

        file.close()