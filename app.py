from flask import Flask,redirect, url_for, render_template, request, flash 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    res = [str(round(sentiment_dict['pos']*100,1)),str(round(sentiment_dict['neu']*100,1)),str(round(sentiment_dict['neg']*100,1))]
    if sentiment_dict['compound'] >= 0.05 :
        res.append("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        res.append("Negative")
    else :
        res.append("Neutral")
    return res

@app.route("/", methods=['POST','GET'])
def hello_world():
    if request.method == "POST":
        data = request.form['data']
        res = sentiment_scores(data)
        print(res)
        return render_template('index.html',data=res)
    return render_template('index.html')