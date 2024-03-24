import argparse
import time
from datetime import datetime
from snoosnooper.script import check_new_posts, read_config
from snoosnooper.utils.utils import subreddit_exists, create_reddit_instance


def main():
    parser = argparse.ArgumentParser(description="Check a subreddit for new posts containing a keyword.")
    parser.add_argument("-s", "--subreddits", nargs="+", required=True, help="The subreddits we're interested in")
    parser.add_argument("-k", "--keywords", nargs="+", required=True, help="The keywords we'er interested in")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    config = read_config()

    # Making sure all subreddits exists before beginning process
    reddit = create_reddit_instance(read_config())
    for subreddit_str in args.subreddits:
        if not subreddit_exists(reddit, subreddit_str):
            raise Exception("Subreddit '%s' doesn't exist; aborting." % subreddit_str)

    while True:
        try:
            formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("\n\nRunning check at %s" % formatted_time)
            check_new_posts(args.subreddits, args.keywords, config, verbose=args.verbose)
            time.sleep(30)
        
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
    
    
