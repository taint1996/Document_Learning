import json

with open('states.json') as f:
  data = json.load(f)
  print(data)

for state in data["states"]:
  print(state['name'], state['lat'])

new_data = json.dumps(data["states"], indent=2, sort_keys=True)
print("-------New Data: %s" % new_data)
