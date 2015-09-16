__author__ = 'tryceo'
import time
import configparser
import praw

config = configparser.ConfigParser()
config.read('logininfo.ini')

r = praw.Reddit(user_agent="imgurgifv")

r.login(config['reddit']['username'], config['reddit']['password'], disable_warning=True)
subredditName = "all"
alreadyDone = []
while True:
    try:
        subreddit = r.get_subreddit(subredditName).get_new(limit=25)
        for submission in subreddit:
            url = submission.url
            id = submission.id
            if id not in alreadyDone and url[-4:] == ".gif" and "imgur.com" in url:
                submission.add_comment("gifv version "
                                       +
                                       url[:-4] + ".gifv")
                alreadyDone.append(id)

        while len(alreadyDone) >= 100:
            del alreadyDone[0]

        time.sleep(10)
    except praw.errors.HTTPException:
        print("HTTP Problem, waiting 15 seconds")
        time.sleep(15)
    except praw.errors.RateLimitExceeded as e:
        if "too much" in e.message:
            time.sleep(60 * 10)
            print(e.message + "\n Waiting 10 minutes")
    except Exception as e:
        print(e)
        time.sleep(30)
