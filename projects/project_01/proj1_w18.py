import webbrowser
import requests
import json

file_object = open("sample_json.txt", "r")
json_string = """{  
   "wrapperType":"track",
   "kind":"song",
   "artistId":136975,
   "collectionId":400835735,
   "trackId":400835962,
   "artistName":"The Beatles",
   "collectionName":"TheBeatles 1967-1970 (The Blue Album)",
   "trackName":"Hey Jude",
   "collectionCensoredName":"The Beatles 1967-1970 (The Blue Album)",
   "trackCensoredName":"Hey Jude",
   "artistViewUrl":"https://itunes.apple.com/us/artist/the-beatles/136975?uo=4",
   "collectionViewUrl":"https://itunes.apple.com/us/album/hey-jude/400835735?i=400835962&uo=4",
   "trackViewUrl":"https://itunes.apple.com/us/album/hey-jude/400835735?i=400835962&uo=4",
   "previewUrl":"https://audio-ssl.itunes.apple.com/apple-assets-us-std-000001/Music/v4/d5/c8/10/d5c81035-a242-c354-45cf-f634e4127f43/mzaf_1171292596660883824.plus.aac.p.m4a",
   "artworkUrl30":"http://is3.mzstatic.com/image/thumb/Music/v4/63/ac/ef/63acef5a-8b6a-b748-5d4c-e6a7e9c13c37/source/30x30bb.jpg",
   "artworkUrl60":"http://is3.mzstatic.com/image/thumb/Music/v4/63/ac/ef/63acef5a-8b6a-b748-5d4c-e6a7e9c13c37/source/60x60bb.jpg",
   "artworkUrl100":"http://is3.mzstatic.com/image/thumb/Music/v4/63/ac/ef/63acef5a-8b6a-b748-5d4c-e6a7e9c13c37/source/100x100bb.jpg",
   "collectionPrice":19.99,
   "trackPrice":1.29,
   "releaseDate":"1968-08-26T07:00:00Z",
   "collectionExplicitness":"notExplicit",
   "trackExplicitness":"notExplicit",
   "discCount":2,
   "discNumber":1,
   "trackCount":14,
   "trackNumber":13,
   "trackTimeMillis":431333,
   "country":"USA",
   "currency":"USD",
   "primaryGenreName":"Rock",
   "isStreamable":true
}"""

class Media(object):
	def __init__(self, title="No Title", author="No Author", release_year = 2018, json = None, link = "itunes.com"):
		if json == None:
			self.title = title
			self.author = author
			self.release_year = release_year
			self.link = link
		else:
			self.title = json["trackName"]
			self.author = json["artistName"]
			self.release_year = json["releaseDate"][:4]
			self.link = json["previewUrl"]
			self.number = 0

	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.release_year)

	def __len__(self):
		return 0

class Song(Media):
	def __init__(self, title ="No Title", author="No Author", release_year = 2018, genre = "None", track_length = 0, album = "No Album", json = None, link = "itunes.com"):
		if json == None:
			super().__init__(title, author, release_year)
			self.genre = genre
			self.track_length = track_length
			self.album = album
		else:
			super().__init__(title, author, release_year, json = json)
			self.genre = json["primaryGenreName"]
			track_length_seconds = json["trackTimeMillis"] / 1000
			self.track_length = track_length_seconds
			self.album = json["collectionName"]

	def __str__(self):
		return super().__str__() + "[" + self.genre + "]"

	def __len__(self):
		return self.track_length

class Movie(Media):
	def __init__(self, title="No Title", author="No Author", release_year = 2018, movie_length = 0, rating = "PG", json = None, link = "itunes.com"):
		if json == None:
			super().__init__(title, author, release_year)
			self.movie_length = movie_length
			self.rating = rating
		else:
			super().__init__(title, author, release_year, json)
			seconds = json["trackTimeMillis"] / 1000
			self.movie_length = round((seconds / 60) )
			self.rating = json["contentAdvisoryRating"]

	def __str__(self):
		return super().__str__() + "[" + self.rating + "]"

	def __len__(self):
		return self.movie_length

json_object =json.loads(json_string)
beatles = Song(json = json_object)
'''print(beatles.album)
print(beatles.__len__())
print(beatles.genre)
print(beatles.__str__())'''
## Other classes, functions, etc. should go here
'''json_object = json.loads(json_string)
jaws = Movie(json = json_object)
print(jaws.title)
print(jaws.author)
print(jaws.release_year)
print(jaws.movie_length)
print(jaws.rating)
'''
def main(last_query = None):
	if last_query != None:
		user_query = last_query
	else:
		user_query = input('Enter a search term, or "exit" to quit: ')
	movies = []
	songs = []
	other_media = []
	if user_query.lower() == "exit":
		print("\nBye!")
		return
	else:
		base_url = "https://itunes.apple.com/search?term="
		user_query = user_query.replace(" ", "+")
		full_url = base_url + user_query
		itunes_result = requests.get(full_url)
		itunes_object = json.loads(itunes_result.text)
		try:
			for result in itunes_object["results"]:
				if result["kind"] == "song":
					songs.append(Song(json = result))
				elif result["kind"] == "feature-movie":
					movies.append(Movie(json = result))
				else:
					other_media.append(Media(json = result))
		except:
			print("\nAn Error occurred!!! Restarting...\n")
			main()

	print("\nSONGS")
	count = 1
	if len(songs) == 0:
		print("No songs found!")
	else:
		for song in songs:
			song.number = count
			print(count, end = " ")
			count += 1
			print(song)
	print("\n")
	print("MOVIES")
	if len(movies) == 0:
		print("No movies found!")
	else:
		for movie in movies:
			movie.number = count
			print(count, end = " ")
			count += 1
			print(movie)
	print("\n")
	print("OTHER MEDIA")
	if len(other_media) == 0 :
		print("No other media found!")
	else:
		for media in other_media:
			media.number = count
			print(count, end = " ")
			count += 1
			print(media)
	user_input = input("\nEnter a number for more info, or another search term, or exit: ")
	if user_input == 'exit':
		print("\nBye!")
		exit()
	
	try:
		for x in songs:
			if x.number == int(user_input):
				print("\n")
				print("Launching")
				print(x.link)
				print("in web browser...\n")
				webbrowser.open(x.link)
		for x in movies:
			if x.number == int(user_input):
				print("\n")
				print("Launching")
				print(x.link)
				print("in web browser...\n")
				webbrowser.open(x.link)
		for x in other_media:
			if x.number == int(user_input):
				print("\n")
				print("Launching")
				print(x.link)
				print("in web browser...\n")
				webbrowser.open(x.link)
	except:
		main(user_input)

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	main()
