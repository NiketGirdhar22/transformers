from typing import Dict
from pydantic import BaseModel
from fastapi import FastAPI
import os
from transformers import pipeline

app = FastAPI()

print("loading tokenizer + model")

CLF = pipeline(
    'text-classification','nt3000/distilbert-toxic-classifier-nt',
    use_fast = True,
    return_all_scores = True,
    use_auth_token = "HF_TOKEN_HERE"
    # for using specifi commit model use: 
    # revision = " COMMIT HASH OF THE DESIRED VERSION "
)

print("Tokenizer and Model loaded")

class Request(BaseModel):
    text: str

class Response(BaseModel):
    probabilities: Dict[str,float]
    label: str
    confidence: float

@app.post("/predict",response_model=Response)
def predict(request: Request):
    output = sorted(CLF(request.text)[0], key=lambda x: x['score'], reverse=True)
    return Response(
        label = output[0]['label'],
        confidence = output[0]['score'],
        probabilities = {item['label'] : item['score'] for item in output}
    )

