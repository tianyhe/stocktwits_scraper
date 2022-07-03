import json
import csv


def to_csv(input_file, output_file, num_twits):
    """Convert the input json file for articles thumbnails to csv file with corresponding headers.
    
    Args:
        input_file (json): the name of the json file to be converted
        output_file (csv): the name of the csv file to write to
        num_articles (int): the number of twits to write to the csv file
    """
    header = ['num', 'id', 'created_at', 'username', 'tag', 'body']
    with open(input_file, 'r') as json_f:
        messages = json.load(json_f)
    with open(output_file, 'w', encoding='UTF8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(header)
        for num in range(num_twits):
            try:
                tag = messages[num]['entities']['sentiment']['basic']
            except:
                tag = 'NULL'
            writer.writerow([
                num, messages[num]['id'], messages[num]['created_at'], tag,
                messages[num]['user']['username'],
                messages[num]['body'].replace('\n', ' ')
            ])
            num += 1