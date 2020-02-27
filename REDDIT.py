
from textblob import TextBlob

import praw
import statistics


reddit = praw.Reddit(client_id='', client_secret="",
                     password='', user_agent='Python',
                     username='')






def search(sub,num=25):
    topic="Post Game Thread:"
    all = reddit.subreddit(sub)
    posts=[]
    my_list1 = []
    with open(topic+".txt","a",encoding="utf8") as myFile:
        for i in all.search(topic, limit=num):
            #print(i.title)
            i.comments.replace_more(limit=0)
            comments = i.comments
            #Possible retrievable information
            posts.append({'title':i.title,'comments':i.comments,'domain':i.domain,'likes':i.likes,'score':i.score,'downs':i.downs,'ups':i.ups,'created_utc':i.created_utc,'num_comments':i.num_comments,'subreddit':i.subreddit})
            for post in posts:
                comments=post['comments']
                myFile.write(post['title']+"\n")
                for comment in comments:
                    attrs = vars(comment)
                    #print(attrs)
                myFile.write(comment.body+"\n")
            tb = TextBlob(comment.body)
            sentiments=(tb.sentiment.polarity)
            #produces more details for each subreddit
            #print("In the post {0} there are {1} comments. The average sentiments of the comments within this post is {2}".format(i.title,i.num_comments,sentiments))
            my_list1.append(sentiments)
        print("Of the Game Threads analyzed in this analysis, the Average sentiment score of this subredditt: {0} is {1}".format(sub,statistics.mean(my_list1)))


search(sub="NFL",num=25)
search(sub="baseball",num=25)
search(sub="soccer",num=25)
search(sub="HOCKEY",num=25)
search(sub="CFB",num=25)
search(sub="NBA",num=25)
search(sub="CollegeBasketball",num=25)

