from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyse_comments(comments):
    sentiment = {'Positive':0,'Negative':0,'Neutral':0}
    for comment in comments:
        analyzer = SentimentIntensityAnalyzer()
        sentiment_score = analyzer.polarity_scores(comment)
        compound_score = sentiment_score["compound"]
        if compound_score >= 0.05:
            sentiment['Positive'] += 1
        elif compound_score <= -0.05:
            sentiment['Negative'] += 1
        else:
            sentiment['Neutral'] += 1
    return sentiment

