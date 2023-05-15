import os
from twilio.rest import Client
import tempfile
import praw


def send_text(config, text_message):
    client = Client(config["Twilio"]["account_sid"], config["Twilio"]["auth_token"])

    message = client.messages.create(
        body=text_message,
        from_=config["Twilio"]["from_number"],
        to=config["Twilio"]["to_number"]
    )

    return message.sid


def record_post_id(seen_posts_data_path, post_id, trim=100):
    # read existing post IDs
    try:
        with open(seen_posts_data_path, "r") as f:
            post_ids = f.read().splitlines()
    except FileNotFoundError:
        post_ids = []

    # add new post ID
    post_ids.append(post_id)

    # trim list to most recent 100 post IDs
    post_ids = post_ids[-trim:]

    # write all post IDs atomically
    with tempfile.NamedTemporaryFile("w", delete=False, dir=".") as f:
        temp_path = f.name
        f.write('\n'.join(post_ids) + "\n")

    os.rename(temp_path, seen_posts_data_path)


def create_reddit_instance(config):
    # creating reddit instance
    reddit = praw.Reddit(
        client_id = config["Reddit"]["client_id"],
        client_secret = config["Reddit"]["client_secret"],
        user_agent = config["Reddit"]["user_agent"]
    )        

    return reddit


def subreddit_exists(reddit, subreddit_str):
    exists = True
    try:
        reddit.subreddits.search_by_name(subreddit_str, exact=True)
    except Exception as e:
        exists = False
    return exists        
