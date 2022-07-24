from api import mean_forex_closing_price
from read_file import process_csv_file
from write_file import report_deficit

def main():
    avg_cp = mean_forex_closing_price()
    days, cash, net_profit, overheads = process_csv_file()
    report_deficit(days, cash, net_profit, overheads, avg_cp)

main()