

"""# **Importing Libraries**"""

import torch
from transformers import RobertaForSequenceClassification, RobertaTokenizerFast

model_path = 'C:\\Users\\Lenovo\\Desktop\\NSU Education\\8th Semester\\CSE299.22\\SavedROBERTA\\model.pth'

"""# **Loading Tuned Model**"""
# Initialize the model architecture
model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=3)  # Use your model's configuration
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')

# Load the state_dict (parameters)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu')))

# Set the model to evaluation mode
model.eval()

"""# **Prediction Test**"""
# Example text for prediction
text = ""
# Tokenize input
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

# Make predictions
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)

if predictions.item() == 0:
    print("Predicted bias: Left")
elif predictions.item() == 1:
    print("Predicted bias: Center")
else:
    print("Predicted bias: Right")
