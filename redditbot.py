import praw
import pdb
import re
import os

reddit = praw.Reddit('yourbotname')

subreddit = reddit.subreddit("test")

if not os.path.isfile('mybotslist.txt') :
    mybotslist=[]

else:
    with open("mybotslist.txt", "r") as f:
        mybotslist = f.read()
        mybotslist = mybotslist.split()
        mybotslist = list(filter(None, mybotslist))

for submission in subreddit.new(limit=10):

    if submission.id not in mybotslist:

        if re.search("is anybody in there", submission.title, re.IGNORECASE) :
            submission.reply("yes im here.. whats up ")
            print("bot commented on : ", submission.title)
            mybotslist.append(submission.id)

with open("mybotslist.txt", "w") as f:
    for post_id in mybotslist :
        f.write(post_id + "\n")


