import pandas as pd

data = {
    'name' : ['A', 'B', 'C'],
    'age' : [30, 20, 20],
    'address': ['pune', 'mumbai', 'CSN']
}

print('student details')
df = pd.DataFrame(data)
print (data)