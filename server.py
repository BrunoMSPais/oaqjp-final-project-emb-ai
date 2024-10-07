from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return"Invalid text! Please try again!"

    formated_response = f"For the given statement, the system response is 'anger'"
    formated_response += f": {response['anger']}, 'disgust': {response['disgust']}, 'fear'"
    formated_response += f": {response['fear']}, 'joy': {response['joy']} and 'sadness'"
    formated_response += f": {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return formated_response

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
