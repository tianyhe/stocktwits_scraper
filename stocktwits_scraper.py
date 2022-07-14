"""The main program of the Stocktwits scraper"""

from datetime import datetime

from src.parser import message_info_to_csv, user_info_to_csv
from src.scraper import scrape


def main():
    """The main function of the scraper"""
    query_symbol = "ETH.X"
    num_twits = 1000

    scrape_time_str = datetime.today().strftime('%Y-%m-%d')
    json_outfile_name: str = f"./data/{scrape_time_str}.json"
    message_csv_outfile_name: str = f"./data/{scrape_time_str}-message.csv"
    user_csv_outfile_name: str = f"./data/{scrape_time_str}-user.csv"

    scrape(json_outfile_name, query_symbol, num_twits)
    message_info_to_csv(json_outfile_name, message_csv_outfile_name, num_twits)
    user_info_to_csv(json_outfile_name, user_csv_outfile_name, num_twits)


if __name__ == "__main__":
    main()
