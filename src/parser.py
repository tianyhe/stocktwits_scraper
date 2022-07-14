import json
import csv


def message_info_to_csv(input_file: str, output_file: str, num_twits: int) -> None:
    """Convert the input json file for twits thumbnails to csv file with corresponding headers.
    This csv file contains information about the twits.

    Args:
        input_file (json): the name of the json file to be converted
        output_file (csv): the name of the csv file to write to
        num_twits (int): the number of twits to write to the csv file
    """
    header = ['num', 'id', 'created_at', 'tag', 'username', 'likes', 'platform', 'body']
    with open(input_file, 'r') as json_f:
        messages = json.load(json_f)
    with open(output_file, 'w', encoding='UTF8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(header)
        for num in range(num_twits):
            message = messages[num]
            user = get_user_info(message)
            id = get_message_id(message)
            timestamp = get_message_timestamp(message)
            tag = get_message_tag(message)
            body = get_message_body(message)
            likes = get_message_likes(message)
            platform = get_message_platform(message)
            username = get_username(user)
            writer.writerow([
                num, id, timestamp, tag, username, likes, platform, body[:30] + '...'
            ])
            num += 1


def user_info_to_csv(input_file: str, output_file: str, num_twits: int) -> None:
    """Convert the input json file for twits thumbnails to csv file with corresponding headers.
    This csv file contains information about the sender of twits.

    Args:
        input_file (json): the name of the json file to be converted
        output_file (csv): the name of the csv file to write to
        num_twits (int): the number of twits to write to the csv file
    """
    header = [
        'num',
        'message_id',
        'tag',
        'user_id',
        'username',
        'join_date',
        'country',
        'followers',
        'following',
        'posts_count',
        'likes_counts',
        'watchlist_counts'
        'platform',
    ]

    with open(input_file, 'r') as json_f:
        messages = json.load(json_f)
    with open(output_file, 'w', encoding='UTF8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(header)
        for num in range(num_twits):
            message = messages[num]
            user = get_user_info(message)
            message_id = get_message_id(message)
            tag = get_message_tag(message)
            user_id = get_user_id(user)
            username = get_username(user)
            join_date = get_user_join_date(user)
            country = get_user_country(user)
            followers = get_user_followers(user)
            following = get_user_following(user)
            posts_count = get_user_posts_count(user)
            likes_count = get_user_likes_count(user)
            watchlist_count = get_user_watchlist_count(user)
            platform = get_message_platform(message)
            writer.writerow([
                num, message_id, tag, user_id, username, join_date, country, followers, following,
                posts_count, likes_count, watchlist_count, platform
            ])
            num += 1


def get_message_id(message):
    """Return the message id from the message.

    Args:
        message (json): the message to get the id from
    Returns:
        message_id (int): the message id
    """
    return message['id']


def get_message_timestamp(message):
    """Return the message timestamp from the message.

    Args:
        message (json): the message to get the timestamp from
    Returns:
        message_timestamp (string): the message timestamp
    """
    return message['created_at']


def get_message_tag(message):
    """Return the message sentiment tag from the message.

    Args:
        message (json): the message to get the tag from
    Returns:
        message_tag (string): the message tag
    """
    try:
        return message['entities']['sentiment']['basic']
    except:
        return "NULL"


def get_message_body(message):
    """Return the message body from the message.

    Args:
        message (json): the message to get the body from
    Returns:
        message_body (string): the message body
    """
    return message['body']


def get_message_likes(message):
    """Return the number of likes the message has received from the message.

    Args:
        message (json): the message to get the like count from
    Returns:
        message_like_count (int): the number of likes the message has received
    """
    try:
        return message['likes']['total']
    except:
        return 0


def get_message_platform(message):
    """Return the message platform from the message.

    Args:
        message (json): the message to get the platform from
    Returns:
        message_platform (string): the message platform
    """
    platform_str = message['source']['title']
    return platform_str.split(' ')[-1]


def get_user_info(message):
    """Return the user info from the message.

    Args:
        message (json): the message to get the user info from
    Returns:
        user_info (json): the user info as a json object
    """
    return message['user']


def get_user_id(user_info):
    """Return the user id from the user info.

    Args:
        user_info (json): the user info to get the id from
    Returns:
        user_id (string): the user id
    """
    return user_info['id']


def get_username(user_info):
    """Return the username from the user info.

    Args:
        user_info (json): the user info to get the name from
    Returns:
        user_name (string): the user name
    """
    return user_info['username']


def get_user_join_date(user_info):
    """Return the user join date from the user info.

    Args:
        user_info (json): the user info to get the join date from
    Returns:
        user_join_date (string): the user join date
    """
    return user_info['join_date']


def get_user_country(user_info):
    """Return the user country from the user info.

    Args:
        user_info (json): the user info to get the country from
    Returns:
        user_country (string): the user country
    """
    try:
        return user_info['home_country']
    except:
        return "NULL"


def get_user_followers(user_info):
    """Return the number of followers of the user from the user info.

    Args:
        user_info (json): the user info to get the followers from
    Returns:
        user_followers (int): the number of followers of the user
    """
    return user_info['followers']


def get_user_following(user_info):
    """Return the number of people the user is following from the user info.

    Args:
        user_info (json): the user info to get the following from
    Returns:
        user_following (int): the number of people the user is following
    """
    return user_info['following']


def get_user_posts_count(user_info):
    """Return the number of posts(twits) the user has created from the user info.

    Args:
        user_info (json): the user info to get the ideas count from
    Returns:
        user_ideas_count (int): the number of post(twits) the user has created
    """
    return user_info['ideas']


def get_user_watchlist_count(user_info):
    """Return the number of stocks the user is watching from the user info.

    Args:
        user_info (json): the user info to get the watchlist count from
    Returns:
        user_watchlist_count (int): the number of stocks the user is watching
    """
    return user_info['watchlist_stocks_count']


def get_user_likes_count(user_info):
    """Return the number of likes the user has given from the user info.

    Args:
        user_info (json): the user info to get the like count from
    Returns:
        user_like_count (int): the number of likes the user has given
    """
    return user_info['like_count']
