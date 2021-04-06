import requests
import json
if __name__=="__main__":
    """ url="http://127.0.0.1/api/Api/clientes/" """
    url="https://jsonplaceholder.typicode.com/posts"
    response=requests.get(url)
    if response.status_code==200:
        response_json=response.json()
        print(response_json)
    
