import datetime as dt
import pprint

import praw
from psaw import PushshiftAPI

import vars

pus = vars.PUS
st = vars.ST
usrn = vars.USRN
pswrd = vars.PSWRD
usragnt = vars.USRAGENT

r = praw.Reddit(client_id=pus, \
                     client_secret= st, \
                     user_agent= usragnt, \
                     username= usrn, \
                     password= pswrd)


api = PushshiftAPI(r)

start_epoch=int(dt.datetime(2021, 6, 1).timestamp())
#print(start_epoch)

testt = list(api.search_submissions(after=start_epoch,
                            subreddit='Munich',
                            #filter=['url','author', 'title', 'subreddit'],
                            limit=3))
print('Number of analyzed posts is ' + len(testt))
for submission in testt:
    submission.comments.replace_more(limit=None)
    n_comments = []
    for comment in submission.comments.list():
        n_comments.append(comment)

    print(submission.score, submission.upvote_ratio, submission.title, submission.link_flair_text, len(n_comments))

#pprint.pprint(testt)