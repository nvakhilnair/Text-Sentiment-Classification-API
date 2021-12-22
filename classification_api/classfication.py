from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def classify(text):
    if(str(type(text)) == "<class 'dict'>"):
        text = list(text.values())[0]
    else:
        pass
    analyser = SentimentIntensityAnalyzer()
    output = analyser.polarity_scores(text)
    if output['compound'] >= 0.05 :
        overall_rating = "Positive"
    elif output['compound'] <= - 0.05 :
        overall_rating = "Negative"
    else :
        output = "Neutral"
    output['overall'] = overall_rating
    return output