''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app : TODO
app = Flask('emotionDetector')
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."
    else:
        return "For given statment, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, 'sadness': {}, The dominant emotion is {}".format(response['anger'],response['disgust'],response['fear'],response['joy'],response['sadness'],response['dominant_emotion'])

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
    app.run(host="0.0.0.0", port=5000)
