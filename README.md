### snoosnooper: It gets the job done.
You're busy, and you want to stay informed about your favorite Reddit communities without getting lost in the noise. That's where snoosnooper comes in. It's essentially a Python script that monitors specific subreddits and alerts you via text message when your chosen keywords are mentioned. It simplifies your digital routine.

### The Name?
The name combines "Snoo" (the Reddit alien) and "snooper" (because the script keeps tabs on subreddits). It's straightforward, and that's all there is to it. Let's proceed.

### Requirements
Check the `requirements.txt` file for the Python packages you need. The key ones are praw (the Reddit API wrapper) and twilio (for text message alerts). Install them using pip:

```bash
pip install -r requirements.txt
```

### Usage
To start, run this command:
```bash
python run.py -s subreddit1 subreddit2 -k keyword1 keyword2
```

Replace subreddit1 and subreddit2 with the subreddits you want to monitor, and keyword1 and keyword2 with the keywords you're tracking. It's straightforward.

### Before You Start
You'll need a few things:
- **Reddit API Account**: Essential for accessing Reddit data. Sign up [here](https://www.reddit.com/wiki/api).
- **Twilio Account**: Needed for sending text notifications. Register [here](https://www.twilio.com).
- **config.ini**: You'll see a file named `config.ini.example`. Fill in your details there, then rename it to `config.ini`. 

Once you've handled these details, you're all set to use snoosnooper.
