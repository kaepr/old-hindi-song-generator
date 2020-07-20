import tensorflow as tf
from tensorflow.keras.models import load_model
from werkzeug.wrappers import Request, Response
from flask import Flask, request, jsonify
import os
from text_clean import clean, clean_song
import numpy as np
from tensorflow.keras.models import load_model
import requests
import uuid
from flask_cors import CORS, cross_origin

app = Flask(__name__,  static_folder = 'build', static_url_path = '/')

CORS(app)
path_to_file = "lyrics2.txt"
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
text = text.replace('\r', '')
#print('Length of the text {} chars'.format(len(text)))
vocab = sorted(set(text))
char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)
text_as_int = np.array([char2idx[c] for c in text])
vocab_size = len(vocab)

model = load_model("lyric_gen2.h5")

def generate_text(model, start_string):
    num_generate = 1000
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []
    temperature = 0.65
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(
            predictions, num_samples=1)[-1, 0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated))

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route('/api/lyrics', methods = ['POST'])
def output_lyrics():
    content = request.get_json()
    initial_string = content["initial_string"]
    initial_string = clean(initial_string)
    full_song = generate_text(model, initial_string)
    song_final = clean_song(full_song)
    response = {"id": str(uuid.uuid4()), "song":song_final}
    return jsonify(response)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False, port = os.environ.get('PORT', 80))
