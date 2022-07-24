"""Functions to get the message and user data fields from the message and user info."""


def get_message_id(message: dict):
    """Return the message id from the message.

    Args:
        message (dict): the message to get the id from
    Returns:
        message_id (int): the message id
    """
    return message['id']


def get_message_timestamp(message: dict):
    """Return the message timestamp from the message.

    Args:
        message (dict): the message to get the timestamp from
    Returns:
        message_timestamp (string): the message timestamp
    """
    return message['created_at']


def get_message_tag(message: dict):
    """Return the message sentiment tag from the message.

    Args:
        message (dict): the message to get the tag from
    Returns:
        message_tag (string): the message tag
    """
    try:
        return message['entities']['sentiment']['basic']
    except:
        return "NULL"


def get_message_body(message: dict):
    """Return the message body from the message.

    Args:
        message (dict): the message to get the body from
    Returns:
        message_body (string): the message body
    """
    message_str = message['body'].strip().replace('\n', ' ')
    return message_str


def get_message_likes(message: dict):
    """Return the number of likes the message has received from the message.

    Args:
        message (dict): the message to get the like count from
    Returns:
        message_like_count (int): the number of likes the message has received
    """
    try:
        return message['likes']['total']
    except:
        return 0


def get_message_platform(message: dict):
    """Return the message platform from the message.

    Args:
        message (dict): the message to get the platform from
    Returns:
        message_platform (string): the message platform
    """
    try:
        platform_str = message['source']['title'].strip().split(' ')[-1]
        return platform_str
    except:
        return 'NULL'


def get_user_info(message: dict):
    """Return the user info from the message.

    Args:
        message (dict): the message to get the user info from
    Returns:
        user_info (json): the user info as a json object
    """
    return message['user']


def get_user_id(user_info: dict):
    """Return the user id from the user info.

    Args:
        user_info (dict): the user info to get the id from
    Returns:
        user_id (string): the user id
    """
    return str(user_info['id'])


def get_username(user_info: dict):
    """Return the username from the user info.

    Args:
        user_info (dict): the user info to get the name from
    Returns:
        user_name (string): the user name
    """
    return user_info['username']


def get_user_join_date(user_info: dict):
    """Return the user join date from the user info.

    Args:
        user_info (dict): the user info to get the join date from
    Returns:
        user_join_date (string): the user join date
    """
    return user_info['join_date']


def get_user_country(user_info: dict):
    """Return the user country from the user info.

    Args:
        user_info (dict): the user info to get the country from
    Returns:
        user_country (string): the user country
    """
    try:
        return user_info['home_country']
    except:
        return "NULL"


def get_user_followers(user_info: dict):
    """Return the number of followers of the user from the user info.

    Args:
        user_info (dict): the user info to get the followers from
    Returns:
        user_followers (int): the number of followers of the user
    """
    return user_info['followers']


def get_user_following(user_info: dict):
    """Return the number of people the user is following from the user info.

    Args:
        user_info (dict): the user info to get the following from
    Returns:
        user_following (int): the number of people the user is following
    """
    return user_info['following']


def get_user_posts_count(user_info: dict):
    """Return the number of posts(twits) the user has created from the user info.

    Args:
        user_info (dict): the user info to get the ideas count from
    Returns:
        user_ideas_count (int): the number of post(twits) the user has created
    """
    return user_info['ideas']


def get_user_watchlist_count(user_info: dict):
    """Return the number of stocks the user is watching from the user info.

    Args:
        user_info (dict): the user info to get the watchlist count from
    Returns:
        user_watchlist_count (int): the number of stocks the user is watching
    """
    return user_info['watchlist_stocks_count']


def get_user_likes_count(user_info: dict):
    """Return the number of likes the user has given from the user info.

    Args:
        user_info (dict): the user info to get the like count from
    Returns:
        user_like_count (int): the number of likes the user has given
    """
    return user_info['like_count']
