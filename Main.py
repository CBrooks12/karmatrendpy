import CONFIG
import praw
import graphing

reddit = praw.Reddit(client_id=CONFIG.client_id,
         client_secret=CONFIG.client_secret,
         password=CONFIG.password,
         user_agent=CONFIG.user_agent,
         username=CONFIG.username)
         
subreddit = reddit.subreddit('programmerhumor')
wordBank = {}
wordBank2 = {}
for submission in subreddit.top(limit=100):
    wordArray = submission.title.split(" ")
    score = submission.score
    for word in wordArray:
        if word in wordBank:
            wordBank[word] += score
            wordBank2[word] += 1
        else:
            wordBank[word] = score
            wordBank2[word] = 1

for key in wordBank:
    wordBank[key] = (wordBank[key]/wordBank2[key])
x = sorted(wordBank.items(), key = lambda x: x[1],reverse=True)
count = 10

words = []
scores = []
occurances = []

for key in x:
    if wordBank2[key[0]] != 1:
        count -= 1;
        words.append(key[0])
        scores.append(key[1])
        occurances.append(wordBank2[key[0]])
        print(key[0], key[1], wordBank2[key[0]])
        if count == 0:
           break
           
graphing.plotData(count, words, scores, occurances)

