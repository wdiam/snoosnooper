# `snoosnooper`: It does the job.

Alright, so you want to know what's happening in your favourite Reddit communities, but you don't have time to sift through all the noise. Enter `snoosnooper`. It's an overglorified Python script that keeps an eye on the subreddits you care about and notifies you (by text message) when certain keywords pop up. Yes, it will make your life easier.

## The Name? Really?

Someone thought it was clever to combine "Snoo" (that's the Reddit alien for the uninitiated) and "snooper" (because that's what this script does - snoop around). So there you have it: `snoosnooper`. Let's move on.

## Requirements

Take a look at the `requirements.txt` file. It has a list of Python packages you need. The main ones are `praw` (that's the Reddit API wrapper) and `twilio` (for the text notifications). Install them with pip:

```bash
pip install -r requirements.txt
```

## Usage

Run this command:

```bash
python run.py -s subreddit1 subreddit2 -k keyword1 keyword2
```

Replace `subreddit1` and `subreddit2` with the subreddits you want to watch, and `keyword1` and `keyword2` with the keywords you're interested in. It's that simple.

## Before You Start

You'll need a couple of things:

1. **Reddit API Account:** Yeah, you need this. Go [here](https://www.reddit.com/wiki/api) and sign up.

2. **Twilio Account:** This is how you get text notifications. Go [here](https://www.twilio.com/try-twilio) and sign up.

3. **config.ini:** Listen, you see that `config.ini.example` file? Yeah, you're going to need to fill in your own details there, and then rename it to `config.ini`. Don't ask why. Just do it.

Do these things, then you can run `snoosnooper`. You're welcome.
