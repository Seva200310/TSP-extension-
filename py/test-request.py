import requests
response=requests.post('http://127.0.0.1:8000/items', json={"listcity":["Москва","Кострома","Санкт-петербург","Архангельск"],"mode":True})
print(response.text)
