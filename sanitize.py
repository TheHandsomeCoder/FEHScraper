import json
from levinstien import findNearestMatch
from pprint import pprint

names = []

with open('./assets/metadata/heroes.json') as data_file:
    names = json.load(data_file)

with open('./rawherodata.json') as hero_json:
    heroes = json.load(hero_json)
    for hero in heroes:
        if hero["name"] not in names:
            hero["name"] = findNearestMatch(hero["name"], names)

    with open('sanatizedherodata.json', 'w') as outfile:
        json.dump(heroes, outfile)

print "done"