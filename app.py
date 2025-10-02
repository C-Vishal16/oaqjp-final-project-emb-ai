from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Home route to render HTML page
@app.route('/')
def home():
    return render_template('index.html')

# API route for emotion detection
@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    text = request.args.get('textToAnalyze')
    if not text:
        return "Error: No text provided", 400

    # Dummy sentiment logic – replace with real NLP model
    if "happy" in text.lower():
        emotion = "Joy"
    elif "angry" in text.lower():
        emotion = "Anger"
    elif "sad" in text.lower():
        emotion = "Sadness"
    else:
        emotion = "Neutral"

    return f"Detected emotion: {emotion}"

if __name__ == '__main__':
    app.run(debug=True)
