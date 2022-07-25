from api import mean_forex_closing_price
from read_file import process_csv_file
from write_file import report_deficit

def main():
    avg_cp = mean_forex_closing_price()
    cash_deficit_list, profit_deficit_list, highest_oh_list = process_csv_file()
    report_deficit(cash_deficit_list, profit_deficit_list, highest_oh_list, avg_cp)

main()