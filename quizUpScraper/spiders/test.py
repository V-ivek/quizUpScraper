import json

with open('./links.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

for l in data['links']:
    print(l)