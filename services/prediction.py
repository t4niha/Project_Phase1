"""# **Importing Libraries**"""
import torch
from transformers import RobertaForSequenceClassification, RobertaTokenizerFast
import time  # Add this import for timing

model_path = 'C:\\Users\\Lenovo\\Desktop\\NSU Education\\8th Semester\\CSE299.22\\SavedROBERTA\\model.pth'

"""# **Loading Tuned Model**"""
# Record start time for model loading
model_load_start = time.time()

# Initialize the model architecture
model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=3)
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')

# Load the state_dict (parameters)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu')))
model.eval()

# Calculate model loading time
model_load_time = time.time() - model_load_start
print(f"Model loading time: {model_load_time:.2f} seconds")

"""# **Prediction Test**"""
# Example text for prediction
text = "President-elect Trump announced two more additions..."  # Your text here

# Record start time for inference
inference_start = time.time()

# Tokenize input
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

# Make predictions
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)

# Calculate inference time
inference_time = time.time() - inference_start
print(f"Inference time: {inference_time:.2f} seconds")

# Print prediction
if predictions.item() == 0:
    print("Predicted bias: Left")
elif predictions.item() == 1:
    print("Predicted bias: Center")
else:
    print("Predicted bias: Right")

# Print total runtime
total_time = model_load_time + inference_time
print(f"Total runtime: {total_time:.2f} seconds")