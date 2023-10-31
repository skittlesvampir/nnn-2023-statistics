#!/usr/bin/python3

import praw
from praw.models import MoreComments
import datetime
from sys import argv
import json

def retrieve_rollcall(day, year):
    reddit = praw.Reddit(
        client_id="client_id",
        client_secret="client_secret",
        user_agent="Python script",
    )
    reddit.read_only = True
    subreddit = reddit.subreddit("nonutnovember")

    date_min = int(datetime.datetime(year, 11, day, 0, 0).strftime("%s"))
    date_max = int(datetime.datetime(year, 11, day, 23, 59).strftime("%s"))

    if year == 2022:
        flair_name = "\"🗳️ Official Roll-Call\""
    elif year == 2023:
        pass # can be done as soon as first roll call was published

    for submission in subreddit.search(f"flair_name: {flair_name}", sort="new"):
        if date_min <= submission.created_utc <= date_max:
            requested_rollcall_post = submission
    requested_rollcall_post = reddit.submission("z8hzit")

    all_comments = []
    
    requested_rollcall_post.comments.replace_more(limit=None)
    for comment in requested_rollcall_post.comments:
        if isinstance(comment, MoreComments):
            continue
        if comment.author == None:
            continue

        all_comments.append({
                                "username": comment.author.name,
                                "text": comment.body
                            })

    all_comments_json = json.dumps(all_comments)

    with open(f"comments/{year}/{day}.json", "w") as file:
        file.write(all_comments_json)

if __name__ == "__main__":
    day = 30
    print(f"Retrieving day {day}...")
    retrieve_rollcall(day, 2022)
