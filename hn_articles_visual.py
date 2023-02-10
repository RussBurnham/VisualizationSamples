import requests
from operator import itemgetter
import plotly.express as px 

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
submission_ids = r.json()

articles = []
for submission_id in submission_ids[:10]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    articles.append(response_dict)

articles_with_descendants = []
for article in articles:
    if 'descendants' in article:
        articles_with_descendants.append(article)
    else:
        print("Article not included:", article['title'])

articles_with_descendants = sorted(articles_with_descendants, key=itemgetter('descendants'), reverse=True)

title = "Top Articles in Hacker News"
labels = {'title': 'Article', 'descendants': '# of Comments'}

fig = px.bar(articles_with_descendants, x='title', y='descendants', title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=14,
    yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
    
fig.show()



