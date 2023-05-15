import praw
import configparser
import os
from pathlib import Path
from .utils.utils import send_text, record_post_id, create_reddit_instance


def get_script_dir():
    return Path(os.path.dirname(os.path.abspath(__file__)))


def read_config():
    # read configuration file
    config_path = get_script_dir().parent / "config.ini"

    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def kw_in_submission(submission, keyword):
        return keyword.lower() in submission.title.lower() or keyword.lower() in submission.selftext.lower()


def check_new_posts(subreddits_str, keywords_str, config, verbose=False):
    # setting up data path and loading up data
    seen_posts_data_path = get_script_dir().parent / "data/seen_posts.txt"

    seen_posts_set = None
    if os.path.exists(seen_posts_data_path):
        with open(seen_posts_data_path, "r") as f:
            seen_posts_set = set(f.read().split("\n"))
    else:
        seen_posts_set = set()


    # creating reddit instance
    reddit = create_reddit_instance(config)
    subreddits = [reddit.subreddit(subreddit_str) for subreddit_str in subreddits_str] 

    for subreddit in subreddits:
        for idx, submission in enumerate(subreddit.new(limit=10)):  
            if verbose:
                print("subreddit: %s, submission %03d, title: %s, id: %s" % (
                    subreddit.display_name, idx, submission.title, submission.id
                ))

            for keyword in keywords_str:
                if kw_in_submission(submission, keyword) and not submission.id in seen_posts_set:
                    if verbose:
                        print("FOUND A MATCH")

                    text_message = "snoosnooper: kw: '%s', subreddit: '%s', post: '%s...'" % (
                        keyword, subreddit.display_name, submission.title[:30]
                    )
                    send_text(config, text_message)

                    seen_posts_set.add(submission.id)
                    record_post_id(seen_posts_data_path, submission.id)
