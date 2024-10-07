import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
    url += 'NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = input_json, headers = header, timeout = 10)

    formated_response = json.loads(response.text)
    emotion_predictions = formated_response['emotionPredictions']
    emotion_predictions_first_instance = emotion_predictions[0]
    emotion_object = emotion_predictions_first_instance['emotion']

    sorted_emotion_object_by_score = sorted(emotion_object.items(), key=lambda x:x[1], reverse=True)

    anger_score = float(emotion_object['anger'])
    disgust_score = float(emotion_object['disgust'])
    fear_score = float(emotion_object['fear'])
    joy_score = float(emotion_object['joy'])
    sadness_score = float(emotion_object['sadness'])
    dominante_emotion = str(sorted_emotion_object_by_score[0][0])

    returned_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominante_emotion
    }

    return returned_response