import torch
from transformers import RobertaForSequenceClassification, RobertaTokenizerFast
from transformers import logging
import time  
def makePrediction(content):   

   
    model_path = 'C:\\Users\\Lenovo\\Desktop\\NSU Education\\8th Semester\\CSE299.22\\SavedROBERTA\\model.pth'

    model_load_start = time.time()

    model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=3)
    tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')

    model.load_state_dict(torch.load(model_path, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu')))
    model.eval()

   
    model_load_time = time.time() - model_load_start
    #print(f"Model loading time: {model_load_time:.2f} seconds")

  
    #text = "President-elect Trump announced two more additions..."  # Your text here

    inference_start = time.time()

    inputs = tokenizer(content, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predictions = torch.argmax(logits, dim=-1)

    inference_time = time.time() - inference_start
    #print(f"Inference time: {inference_time:.2f} seconds")

   
    # if predictions.item() == 0:
    #     print("Predicted bias: Left")
    # elif predictions.item() == 1:
    #     print("Predicted bias: Center")
    # else:
    #     print("Predicted bias: Right")


    total_time = model_load_time + inference_time
    #print(f"Total runtime: {total_time:.2f} seconds")
    logging.set_verbosity_warning()
    return predictions.item()
