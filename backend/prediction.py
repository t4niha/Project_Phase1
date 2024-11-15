

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
text = "President-elect Trump announced two more additions to his White House staff on Friday, promoting his campaign spokesman to lead the communications shop.Trump announced that Steven Cheung would return to the White House as assistant to the president and director of communications. Cheung previously served as communications director for the Trump-Vance campaign and was the White House director of strategic response in Trump's first term.Additionally, Trump confirmed that Sergio Gor will join the White House as director of the presidential personnel office. Gor, an ally and business partner of Donald Trump Jr.'s, was in charge of the pro-Trump political action committee Right For America and previously worked in Republican Sen. Rand Paul's office. Steven Cheung and Sergio Gor have been trusted Advisors since my first Presidential Campaign in 2016, and have continued to champion America First principles throughout my First Term, all the way to our HIstoric Victory in 2024, Trump said in a statement. I am thrilled to have them join my White House, as we Make America Great Again!" 
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
