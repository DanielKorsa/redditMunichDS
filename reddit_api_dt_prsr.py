import datetime as dt
import pprint

import praw
import pandas as pd
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

start_epoch=int(dt.datetime(2021, 1, 1).timestamp())
#print(start_epoch)

testt = list(api.search_submissions(after=start_epoch,
                            subreddit='Munich',
                            #filter=['url','author', 'title', 'subreddit'],
                            limit=1000))
print('Number of analyzed posts is ' + str(len(testt)))

parsed_dict = {}
parsed_dt = []

for submission in testt:
    submission.comments.replace_more(limit=None)
    n_comments = []
    for comment in submission.comments.list():
        n_comments.append(comment)
    #print(type(submission.score))
    parsed_dict = {}
    parsed_dict['upvotes'] = submission.score
    parsed_dict['upvoteRatio'] = submission.upvote_ratio
    parsed_dict['flair'] = submission.link_flair_text
    parsed_dict['title'] = submission.title
    parsed_dict['commentsNumber'] = len(n_comments)

    parsed_dt.append(parsed_dict)
    #print(submission.score, submission.upvote_ratio, submission.title, submission.link_flair_text, len(n_comments))


#rdt_dt = pd.DataFrame.from_dict(parsed_dict, orient='index')
rdt_dt = pd.DataFrame(parsed_dt)
rdt_dt.to_csv('data\MunichParsedDt.csv', sep='\t', encoding='utf-8', index=True)

#pprint.pprint(testt)