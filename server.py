'''Executing this will start a server on PORT 5000 that will consume the Watson AI libraries
API and wil return an emotion analysis on a given text to be analyzed.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detection():
    '''This function reads the "textToAnalyze" route param to return an emotion analysis 
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return"Invalid text! Please try again!"

    formated_response = "For the given statement, the system response is 'anger'"
    formated_response += f": {response['anger']}, 'disgust': {response['disgust']}, 'fear'"
    formated_response += f": {response['fear']}, 'joy': {response['joy']} and 'sadness'"
    formated_response += f": {response['sadness']}. The dominant emotion is "
    formated_response += f"{response['dominant_emotion']}."

    return formated_response

@app.route("/")
def render_index_page():
    '''This function renders the template file "index.html"
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
