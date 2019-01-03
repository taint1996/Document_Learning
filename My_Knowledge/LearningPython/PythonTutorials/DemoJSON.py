''' JavaScript Object Notation '''
import json

people_string = '''
{
  "people": [
    {
      "name": "Tai Beo",
      "phone": "0898-679-723",
      "email": "taibeoka1996@gmail.com",
      "has_license": false
    },
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "email": ["johnsmith@boguse.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Elizabeth",
      "phone": "615-555-7164",
      "email": null,
      "has_license": false
    }
  ]
}
'''

data = json.loads(people_string)

for person in data["people"]:
  print("Data People: %s" % person['name'])
  del person['phone']

new_string = json.dumps(data, sort_keys=True, indent=2)
print(new_string)

