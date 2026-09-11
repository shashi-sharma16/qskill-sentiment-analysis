from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    polarity = None
    subjectivity = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        blob = TextBlob(text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

    return render_template(
        "index.html",
        text=text,
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity
    )

if __name__ == "__main__":
    app.run(debug=True)

