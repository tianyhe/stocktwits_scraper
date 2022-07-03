import json


def add_to_json(json_file, elements):
    """Append a list of elements to a json file, if the file does not exist, create it and add the elements

    Args:
        json_file (json): the file path of the json file
        elements (List): a list of elements to append to the json file
    """
    try:
        with open(json_file, 'r+') as outfile:
            j = json.load(outfile)
            outfile.seek(0)
            for element in elements:
                j.append(element)
            json.dump(j, outfile, indent=4)
    except FileNotFoundError:
        with open(json_file, 'w') as outfile:
            json.dump(elements, outfile, indent=4)