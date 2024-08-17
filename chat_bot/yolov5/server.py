from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
from io import BytesIO
import logging
import torch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return "FastAPI"

@app.post("/predict")
async def process_home_form(file: UploadFile = File(...),
                             model_name: str = Form(...)):
    logger.info(f"Model name: {model_name}")

    model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)
    labels = model.names
    logger.info(f"Labels: {labels}")

    results = model(Image.open(BytesIO(await file.read())))

    json_results = results_to_json(results,model)
    
    return json_results

def results_to_json(results, model):
    return [
        [
          {
          "class": int(pred[5]),
          "class_name": model.model.names[int(pred[5])],
          "bbox": [int(x) for x in pred[:4].tolist()], # convert bbox results to int from float
          "confidence": float(pred[4]),
          }
        for pred in result
        ]
      for result in results.xyxy
      ]

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(host='localhost', port=8000, reload=True, workers=1)