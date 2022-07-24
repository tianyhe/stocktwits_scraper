"""The main program of the Stocktwits scraper"""

from datetime import datetime

from src.utils import message_info_to_csv, user_info_to_csv, add_user_info_to_json, add_message_to_json
from src.scraper import scrape


def main():
    """The main function of the scraper"""
    query_symbol = "ETH.X"
    num_twits = 5000
    scrape_time_str = datetime.today().strftime('%Y-%m-%d')

    # File names
    scraped_message_json_outfile_name: str = f"./data/scrape_data/{scrape_time_str}.json"
    scraped_message_csv_outfile_name: str = f"./data/scrape_data/{scrape_time_str}-message.csv"
    message_json_outfile_name: str = f"./data/message.json"
    message_csv_outfile_name: str = f"./data/message.csv"
    user_json_outfile_name: str = f"./data/user.json"
    user_csv_outfile_name: str = f"./data/user.csv"

    # Scrape the messages
    scrape(scraped_message_json_outfile_name, query_symbol, num_twits)

    # Add the scraped messages and corresponding user info to the json files
    add_user_info_to_json(scraped_message_json_outfile_name, user_json_outfile_name)
    add_message_to_json(scraped_message_json_outfile_name, message_json_outfile_name)

    # Convert the new scraped messages to a csv file and name by the scrape time
    message_info_to_csv(scraped_message_json_outfile_name, scraped_message_csv_outfile_name)
    # Convert all scraped messages up to the new scrape time to a csv file
    message_info_to_csv(message_json_outfile_name, message_csv_outfile_name)
    # Convert all scraped user info to the new scrape time to a csv file
    user_info_to_csv(user_json_outfile_name, user_csv_outfile_name)


if __name__ == "__main__":
    main()
