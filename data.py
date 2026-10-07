import pandas as pd
import requests

data = {
    'name' : ['A', 'B', 'C'],
    'age' : [30, 20, 20],
    'address': ['pune', 'mumbai', 'CSN']
}

print('student details')
df = pd.DataFrame(data)
print (data)

print('API data')
response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response.json())