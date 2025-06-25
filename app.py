from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import pickle
import re
import string
from keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

model = tf.keras.models.load_model('incident_response_model.keras')

with open('tokenizer_desc.pkl', 'rb') as f:
    tokenizer_desc = pickle.load(f)

with open('mlb.pkl', 'rb') as f:
    mlb = pickle.load(f)

max_desc_length = 17
max_summary_length = 14
max_response_length = 9
max_action_length = 7

def clean_text(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_incident_and_generate_action(description, threshold=0.3):
    cleaned_description = clean_text(description)
    sequence = tokenizer_desc.texts_to_sequences([cleaned_description])
    padded_sequence = pad_sequences(sequence, maxlen=max_desc_length, padding='post', truncating='post')
    dummy_action_input = np.zeros((1, max_action_length))

    y_pred_probs = model.predict([padded_sequence , dummy_action_input])[0]
    classification_probs = y_pred_probs[0]

    predicted_labels_indices = np.where(classification_probs > threshold)[0]

    if len(predicted_labels_indices) == 0:
        return ["Unknown"], "Response team dispatched to the scene."

    predicted_labels_binary = np.zeros((1, len(mlb.classes_)))
    predicted_labels_binary[0, predicted_labels_indices] = 1
    predicted_labels = mlb.inverse_transform(predicted_labels_binary)[0]

    if len(predicted_labels) == 1:
        message = f"{predicted_labels[0].title()} team dispatched."
    else:
        message = ", ".join([label.title() for label in predicted_labels]) + " teams dispatched."

    return predicted_labels, message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        description = request.form['description']
        predicted_labels, action_message = predict_incident_and_generate_action(description)
        return render_template('result.html', labels=predicted_labels, action=action_message)
if __name__ == '__main__':
    app.run(debug=True)
