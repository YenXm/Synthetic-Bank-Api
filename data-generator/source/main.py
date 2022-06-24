import classes
import json
import requests
import constant


generator = classes.Generactor()

person_dict: dict = generator.generate_data(constant.AMOUNT_OF_PERSON)

json_string = json.dumps([x for x in person_dict])

with open('data.json', 'w') as f:
    f.write(json_string)

# Somehow the json data is Invalid here put taking the data from the file and manually calling the route work correctly.
# print(requests.post(constant.API_ROUTE, json=json_string, verify=False).text)
