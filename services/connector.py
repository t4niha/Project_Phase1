from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load model and tokenizer
model_path = '/content/drive/MyDrive/path_to_your_saved_model'
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model.eval()

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    # Tokenize and predict
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()

    # Map prediction to bias label
    label_map = {0: 'left', 1: 'center', 2: 'right'}
    result = label_map[prediction]
    return jsonify({'bias': result})

if __name__ == '__main__':
    app.run(debug=True)

