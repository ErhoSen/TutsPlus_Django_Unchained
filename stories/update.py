import feedparser
from pprint import pprint as pp

# Setup the Django environment so we can access our models
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HackerNews.settings')

from django.contrib.auth.models import User
import django

from stories.models import Story

PROTO = "https://"
USERNAME = "botabormot@gmail.com"
PASSWORD = "gAx4BiM7th64KTn"
PATH = "mail.google.com/gmail/feed/atom"

AUTHORS = {"erhosen@gmail.com": "Jesussy", "semen995@gmail.com": "Semen995"}

def get_new_posts():
    feed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + PATH)
    # mailcount = feed["feed"]["fullcount"]

    # pp(feed)

    author = feed.entries[0]["author_detail"]["email"] # == "erhosen@gmail.com"

    data = feed.entries[0]["summary"].split(" ")
    link = data[-4]
    title = " ".join(data[:-4])
    return author, link, title

def main():
    author, link, title = get_new_posts()

    # Add the stories to the database
    moderator = User.objects.get(username=AUTHORS[author])
    story = Story(
        title=title,
        url=link,
        moderator=moderator)
    story.save()

if __name__ == '__main__':
    django.setup()
    main()