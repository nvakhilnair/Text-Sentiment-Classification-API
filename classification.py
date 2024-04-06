from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Classifier:
    def __init__(self) -> None:
        self.analyser = SentimentIntensityAnalyzer()

    async def classify(self, text):
        output = self.analyser.polarity_scores(text)
        if output['compound'] >= 0.05 :
            return "Positive"
        elif output['compound'] <= - 0.05 :
            return "Negative"
        return "Neutral"