"""The main program of the Stocktwits scraper"""

from datetime import datetime

from src.export import to_csv
from src.scraper import scrape


def main():
    """The main function of the scraper"""
    query_symbol = "ETH.X"
    num_twits = 1000

    scrape_time_str = datetime.today().strftime('%Y-%m-%d')
    json_outfile_name = f"./data/{scrape_time_str}.json"
    csv_outfile_name = f"./data/{scrape_time_str}.csv"

    scrape(json_outfile_name, query_symbol, num_twits)
    to_csv(json_outfile_name, csv_outfile_name, num_twits)


if __name__ == "__main__":
    main()
