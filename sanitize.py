import json
from levinstien import findNearestMatch
from pprint import pprint

names = []
weapons = []
assists = []
specials = []
passives = []
seals = []

with open('./assets/metadata/heroes.json') as data_file:
    names = json.load(data_file)

with open('./assets/metadata/weapons.json') as data_file:
    weapons = json.load(data_file)

with open('./assets/metadata/assists.json') as data_file:
    assists = json.load(data_file)

with open('./assets/metadata/specials.json') as data_file:
    specials = json.load(data_file)

with open('./assets/metadata/passives.json') as data_file:
    passives = json.load(data_file)

with open('./assets/metadata/seals.json') as data_file:
    seals = json.load(data_file)

with open('./rawherodata.json') as hero_json:
    heroes = json.load(hero_json)
    for hero in heroes:
        # if hero["name"] not in names:
        #     match = findNearestMatch(hero["name"], names)
        #     print hero["name"] + ' -> ' + match
        #     hero["name"] = match

        # if hero["weapon"] != "_" and hero["weapon"] not in weapons:
        #     match = findNearestMatch(hero["weapon"], weapons)
        #     print hero["weapon"] + ' -> ' + match
        #     hero["weapon"] = match

        # if hero["assist"] != "_" and hero["assist"] not in assists:
        #     match = findNearestMatch(hero["assist"], assists)
        #     print hero["assist"] + ' -> ' + match
        #     hero["assist"] = match

        # if hero["special"] != "_" and hero["special"] not in specials:
        #     match = findNearestMatch(hero["special"], specials)
        #     print hero["special"] + ' -> ' + match
        #     hero["special"] = match

        # if hero["aSlot"] != "_" and hero["aSlot"] not in passives:
        #     match = findNearestMatch(hero["aSlot"], passives)
        #     print hero["aSlot"] + ' -> ' + match
        #     hero["aSlot"] = match

        # if hero["bSlot"] != "_" and hero["bSlot"] not in passives:
        #     match = findNearestMatch(hero["bSlot"], passives)
        #     print hero["bSlot"] + ' -> ' + match
        #     hero["bSlot"] = match

        # if hero["cSlot"] != "_" and hero["cSlot"] not in passives:
        #     match = findNearestMatch(hero["cSlot"], passives)
        #     print hero["cSlot"] + ' -> ' + match
        #     hero["cSlot"] = match

        # if hero["sSlot"] != "_" and hero["sSlot"] not in seals:
        #     match = findNearestMatch(hero["sSlot"], seals)
        #     print hero["sSlot"] + ' -> ' + match
        #     hero["sSlot"] = match
        print hero["exp"]

    with open('sanatizedherodata.json', 'w') as outfile:
        json.dump(heroes, outfile)

print "done"