import pytest
from snoosnooper.script import read_config
from snoosnooper.utils.utils import create_reddit_instance, subreddit_exists


def test_subreddit_exists_true():
    config = read_config()
    reddit = create_reddit_instance(config)
    assert subreddit_exists(reddit, "hardwareswap")


def test_subreddit_exists_false():
    config = read_config()
    reddit = create_reddit_instance(config)
    assert not subreddit_exists(reddit, "asdfwer@#Q$")


