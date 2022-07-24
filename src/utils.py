import csv
import json

import src.parser as parser


def add_to_json(json_file: str, elements) -> None:
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


def add_message_to_json(input_file: str, message_file: str) -> None:
    """Add scraped messages to the message file that stored all previous scraped messages.

    Args:
        input_file (json): the new scraped message json file to add to the message file
        message_file (json): the json file to store all user_info information
    """
    with open(input_file, 'r') as messages_f:
        messages = json.load(messages_f)
    try:
        messages_f = open(message_file, 'r+')
        messages_json = json.load(messages_f)
        messages_f.seek(0)
    except FileNotFoundError:
        messages_f = open(message_file, 'w')
        messages_json = []
    messages_json.extend(messages)
    json.dump(messages_json, messages_f, indent=4)
    print('Added {} messages to the message file'.format(len(messages)))
    messages_f.close()


def add_user_info_to_json(input_file: str, user_file: str) -> None:
    """Extract user info from the newly scraped message json file and add it to the user file.

    Args:
         input_file (json): the new scraped message json file to extract user info
         user_file (json): the json file to store all user_info information
    """
    with open(input_file, 'r') as messages_f:
        messages = json.load(messages_f)
    try:
        users_f = open(user_file, 'r+')
        users = json.load(users_f)
        users_f.seek(0)
    except FileNotFoundError:
        users_f = open(user_file, 'w')
        users = {}
    added_users = extract_user_info_from_message(messages, users)
    json.dump(users, users_f, indent=4)
    print('Added {} users to the user file'.format(added_users))
    users_f.close()


def extract_user_info_from_message(messages: list, users: dict):
    """Extract user info from the message and add it to the user file.
    If the user is not in the user file, add it. Otherwise, update the user information.

    Args:
        messages (list): the message json file to extract user info (in the form of a list)
        users (dict): the user json file to store user info (in the form of a dictionary)
    Returns:
        added_users (int): the number of users added to the user file
    """
    added_users = 0
    for message in messages:
        user = parser.get_user_info(message)
        user_id = parser.get_user_id(user)
        username = parser.get_username(user)
        join_date = parser.get_user_join_date(user)
        country = parser.get_user_country(user)
        followers = parser.get_user_followers(user)
        following = parser.get_user_following(user)
        posts_count = parser.get_user_posts_count(user)
        likes_count = parser.get_user_likes_count(user)
        watchlist_count = parser.get_user_watchlist_count(user)
        platform = parser.get_message_platform(message)
        if user_id in users.keys():
            update_user_info(users, user_id, username, join_date, country, followers, following, posts_count,
                             likes_count, watchlist_count, platform)
        else:
            add_user_info(users, user_id, username, join_date, country, followers, following, posts_count, likes_count,
                          watchlist_count, platform)
            added_users += 1
    return added_users


def update_user_info(users: dict, user_id, username, join_date, country, followers, following, posts_count, likes_count,
                     watchlist_count, platform):
    """Update the user info in the user file.

    Args:
         users (json): the json file to store all user_info information
         user_id (str): the user id
         username (str): the user name
         join_date (str): the user join date
         country (str): the user country
         followers (int): the user followers
         following (int): the user following
         posts_count (int): the user posts count
         likes_count (int): the user likes count
         watchlist_count (int): the user watchlist count
         platform (str): the user platform
    """
    users[user_id]['username'] = username
    users[user_id]['join_date'] = join_date
    users[user_id]['country'] = country
    users[user_id]['followers'] = followers
    users[user_id]['following'] = following
    users[user_id]['posts_count'] = posts_count
    users[user_id]['likes_count'] = likes_count
    users[user_id]['watchlist_count'] = watchlist_count
    users[user_id]['platform'] = platform


def add_user_info(users: dict, user_id, username, join_date, country, followers, following, posts_count, likes_count,
                  watchlist_count, platform):
    """Add the user info to the user file.

    Args:
         users (json): the json file to store all user_info information
         user_id (str): the user id
         username (str): the user name
         join_date (str): the user join date
         country (str): the user country
         followers (int): the user followers
         following (int): the user following
         posts_count (int): the user posts count
         likes_count (int): the user likes count
         watchlist_count (int): the user watchlist count
         platform (str): the user platform
    """
    users[user_id] = {
        'username'       : username,
        'join_date'      : join_date,
        'country'        : country,
        'followers'      : followers,
        'following'      : following,
        'posts_count'    : posts_count,
        'likes_count'    : likes_count,
        'watchlist_count': watchlist_count,
        'platform'       : platform
    }


def user_info_to_csv(user_file: str, output_file: str) -> None:
    """Convert the input json file for twits thumbnails to csv file with corresponding headers.
    This csv file contains information about the sender of twits.

    Args:
        user_file (json): the json file that stores all user_info information
        output_file (csv): the name of the csv file to write to
    """
    header = [
        'num',
        'user_id',
        'username',
        'join_date',
        'country',
        'followers',
        'following',
        'posts_count',
        'likes_counts',
        'watchlist_counts',
        'platform',
    ]

    with open(user_file, 'r') as json_f:
        users = json.load(json_f)
    with open(output_file, 'w', encoding='UTF8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(header)
        num = 0
        for user in users:
            num += 1
            user_id = user
            username = users[user]['username']
            join_date = users[user]['join_date']
            country = users[user]['country']
            followers = users[user]['followers']
            following = users[user]['following']
            posts_count = users[user]['posts_count']
            likes_count = users[user]['likes_count']
            watchlist_count = users[user]['watchlist_count']
            platform = users[user]['platform']
            writer.writerow([
                num, user_id, username, join_date, country, followers, following,
                posts_count, likes_count, watchlist_count, platform
            ])


def message_info_to_csv(input_file: str, output_file: str) -> None:
    """Convert the input json file for twits thumbnails to csv file with corresponding headers.
    This csv file contains information about the twits.

    Args:
        input_file (json): the name of the json file to be converted
        output_file (csv): the name of the csv file to write to
    """
    header = ['num', 'message_id', 'created_at', 'tag', 'username', 'user_id', 'likes', 'platform', 'body']
    with open(input_file, 'r') as json_f:
        messages = json.load(json_f)
    with open(output_file, 'w', encoding='UTF8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(header)
        for num in range(len(messages)):
            message = messages[num]
            user = parser.get_user_info(message)
            message_id = parser.get_message_id(message)
            timestamp = parser.get_message_timestamp(message)
            tag = parser.get_message_tag(message)
            body = parser.get_message_body(message)
            likes = parser.get_message_likes(message)
            platform = parser.get_message_platform(message)
            username = parser.get_username(user)
            user_id = parser.get_user_id(user)
            writer.writerow([
                num, message_id, timestamp, tag, username, user_id, likes, platform, body
            ])
