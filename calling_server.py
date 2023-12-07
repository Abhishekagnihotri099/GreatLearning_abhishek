import requests

r = requests.post('http://127.0.0.1:5000/get_predictions', json={'SepalLengthCm': 5.1, 'SepalWidthCm': 3.5, 'PetalLengthCm': 1.4, 'PetalWidthCm': 0.2})
r.status_code
r.text

