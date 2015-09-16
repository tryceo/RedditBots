__author__ = 'tryceo'
import time

import praw

from emailer import sendalert

r = praw.Reddit(user_agent="alertme")

alreadyDone = []
while True:
    try:
        subreddit = r.get_subreddit("buildapcsales").get_new(limit=25)
        for submission in subreddit:
            url = submission.url
            id = submission.id
            title = submission.title
            titlelowercase = title.lower()
            redditurl = submission.permalink

            if id not in alreadyDone and ('gpu' or 'g27' or 'racing' or 'wheel') in titlelowercase:
                sendalert("Title : " + title + " URL : " + url + " Reddit: " + redditurl)
                alreadyDone.append(id)

        while len(alreadyDone) >= 50:
            del alreadyDone[0]
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
