from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_joy_emotion_detector(self):
        joy_emotion_detection = emotion_detector('I am glad this happened')
        self.assertEqual(joy_emotion_detection['dominant_emotion'], 'joy')
        
    def test_anger_emotion_detector(self):
        anger_emotion_detection = emotion_detector('I am really mad about this')
        self.assertEqual(anger_emotion_detection['dominant_emotion'], 'anger')
        
    def test_disgust_emotion_detector(self):
        disgust_emotion_detection = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust_emotion_detection['dominant_emotion'], 'disgust')
        
    def test_sadness_emotion_detector(self):
        sadness_emotion_detection = emotion_detector('I am so sad about this')
        self.assertEqual(sadness_emotion_detection['dominant_emotion'], 'sadness')
        
    def test_fear_emotion_detector(self):
        fear_emotion_detection = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear_emotion_detection['dominant_emotion'], 'fear')

unittest.main()
