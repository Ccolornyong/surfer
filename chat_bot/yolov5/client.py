import requests as r
import json
from pprint import pprint

def send_request(image = './car.jpg', model_name = 'yolov5s'):
    res = r.post("http://localhost:8000/predict", 
                    data={'model_name': model_name}, 
                    files = {'file': open(image , "rb")}
                    )

    pprint(json.loads(res.text))

if __name__ == '__main__':
    send_request()