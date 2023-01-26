# Project Overview
https://www.youtube.com/watch?v=ulFlr6uGwlw

# Inspiration
The abundance of contradictory articles on the internet which skew perception of the overall market

# What it does
Gives a reading of the current market sentiment based on news articles and Reddit posts from the r/stocks subreddit.

# How we built it
## Technology

- Used Cohere to build a classification model trained on news article headlines and Reddit posts, to analyze the sentiment of the current market.
- Used Redis to manage the job queue for jobs that run the classification algorithm.
- Used Netlify to host the frontend
- Used Heroku to host the backend

## Backend

- Flask

## Frontend

- React with Typescript
- Used ChartJS to create the graph that showcases the sentiment changes over the past week.

## Database

- MongoDB

## APIs

- Reddit API to aggregate posts from reddit.
- Free News API by Newscatcher API to aggregate news articles.

# Challenges we ran into

- Since we used a lot of different technologies for the first time, we had to allocate more of our time to learning them.
- We also had to spend time to fine tune the classification model so that it can correctly identify the sentiment based on the news article or Reddit post.

# Accomplishments that we're proud of

We are proud that we generated accurate sentiment ratings for the news articles and Reddit posts.

# What we learned

We learned how to use Redis to schedule the time-consuming classification jobs, so that it runs in the background.

# What's next for Sentiment Index
We want to add the ability to generate sentiment analysis of individual stocks.
