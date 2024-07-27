from flask import Flask, request, render_template, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# OpenAI API key (replace with your actual API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Text generation route
@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify({'generated_text': response.choices[0].text.strip()})

# Text summarization route
@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.form['text']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n{text}",
        max_tokens=100
    )
    return jsonify({'summary': response.choices[0].text.strip()})

# Language translation route
@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    target_language = request.form['language']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the following text to {target_language}:\n{text}",
        max_tokens=150
    )
    return jsonify({'translation': response.choices[0].text.strip()})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
