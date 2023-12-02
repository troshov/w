import requests
import json

data = json.loads(requests.get('https://swapi.dev/api/starships/10').text)

pilots = []

for pilot in data['pilots']:
    pilot_info_all = json.loads(requests.get(pilot).text)
    pilot_info = {'name': pilot_info_all['name'],
                  'height':pilot_info_all['height'],
                  'mass': pilot_info_all['mass'],
                  'homeworld': json.loads(requests.get(pilot_info_all['homeworld']).text)['name'],
                  'homeworld_url': pilot_info_all['homeworld']}
    pilots.append(pilot_info)
    

new_data = {'name': data['name'],
            'max_atmosphering_speed': data['max_atmosphering_speed'],
            'starship_class': data['starship_class'],
            'pilots': pilots}

with open('info_starship.json', 'w') as file:
    json.dump(new_data, file, indent=4)


print(json.dumps(new_data, indent=4))