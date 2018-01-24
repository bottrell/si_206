#overloaded assignment/ length/ string/ contains methods
#swapi.co
import requests
import json


url_to_name = {"https://swapi.co/api/species/1/" : "Human",
				"https://swapi.co/api/species/2/" : "Droid"}

def get_name_from_url(url):
	if url in url_to_name:
		return url_to_name[url]
	else:
		return "Other"

class Character:
	def __init__(self, name_in = "Luke", species_in="Human", json_dict = "None"):
		if json_dict is not None:
			self.name = json_dict["name"]
			sp_url = json_dict["species"][0]
			self.species = get_name_from_url(sp_url)
		else:
			self.name = name_in
			self.species = species_in

	def __str__(self):
		return 'I am ' + self.name + ' and I am a ' + self.species

class Human(Character):
	def __init__(self, name_in = "Luke", species_in="Human", json_dict = "None", eye_color = "Brown"):
		super().__init__(name_in, species_in, json_dict)
		if json_dict != None:
			self.eye_color = json_dict["eye_color"]

	def __str__(self):
		return super().__str__() + " and I have " + self.eye_color + " eyes"


base_people_url = "https://swapi.co/api/people/"
r = requests.get(base_people_url)
#print(r.text)

json_dict = json.loads(r.text)
character_list = json_dict["results"]
characters = []

for character_dict in character_list:
	species = get_name_from_url(character_dict["species"][0])
	if species == "Human":
		c = Human(json_dict = character_dict)
	else:
		c = Character(json_dict = character_dict)
	characters.append(c)


