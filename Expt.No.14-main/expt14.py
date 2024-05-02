pip install textblob

from textblob import TextBlob

Feedback1 = "The Food at Radison was awesome"
Feedback2 = "The Food at Radison was very good"

blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)

blob1.sentiment

blob2.sentiment
