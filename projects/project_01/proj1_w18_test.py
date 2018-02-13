import unittest
import json
import requests
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

# ------------ TESTS FOR PART 1 ------------
    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")

    def testMediaConstructor(self):
    	media1 = proj1.Media()
    	media2 = proj1.Media("Real Friends")
    	media3 = proj1.Media("Real Friends", "Kanye West")
    	media4 = proj1.Media("Real Friends", "Kanye West", 2016)

    	#testing title
    	self.assertEqual(media1.title, "No Title")
    	self.assertEqual(media2.title, "Real Friends")
    	self.assertEqual(media3.title, "Real Friends")
    	self.assertEqual(media4.title, "Real Friends")

    	#testing artist
    	self.assertEqual(media1.author, "No Author")
    	self.assertEqual(media2.author, "No Author")
    	self.assertEqual(media3.author, "Kanye West")
    	self.assertEqual(media4.author, "Kanye West")

    	#testing release year
    	self.assertEqual(media1.release_year, 2018)
    	self.assertEqual(media2.release_year, 2018)
    	self.assertEqual(media3.release_year, 2018)
    	self.assertEqual(media4.release_year, 2016)

    def testSongConstructor(self):
        song1 = proj1.Song()
        song2 = proj1.Song("Facts")
        song3 = proj1.Song("Heartless", "Kanye West")
        song4 = proj1.Song("FML", "Kanye West", 2016)
        song5 = proj1.Song("Stronger", "Kanye West", 2006, "Rap")
        song6 = proj1.Song("Fade", "Kanye West", 2016, "Rap", album = "The Life of Pablo")
        song7 = proj1.Song("Famous", "Kanye West", 2016, "Rap", 1127625, "The Life of Pablo")
    	
    	#testing title
        self.assertEqual(song1.title, "No Title")
        self.assertEqual(song2.title, "Facts")
        self.assertEqual(song3.title, "Heartless")
        self.assertEqual(song4.title, "FML")
        self.assertEqual(song5.title, "Stronger")
        self.assertEqual(song6.title, "Fade")
        self.assertEqual(song7.title, "Famous")
        #testing artist
        self.assertEqual(song1.author, "No Author")
        self.assertEqual(song2.author, "No Author")
        self.assertEqual(song3.author, "Kanye West")
        self.assertEqual(song4.author, "Kanye West")
        self.assertEqual(song5.author, "Kanye West")
        self.assertEqual(song6.author, "Kanye West")
        self.assertEqual(song7.author, "Kanye West")
    	#testing year
        self.assertEqual(song1.release_year, 2018)
        self.assertEqual(song2.release_year, 2018)
        self.assertEqual(song3.release_year, 2018)
        self.assertEqual(song4.release_year, 2016)
        self.assertEqual(song5.release_year, 2006)
        self.assertEqual(song6.release_year, 2016)
        self.assertEqual(song7.release_year, 2016)
    	#testing genre
        self.assertEqual(song1.genre, "None")
        self.assertEqual(song2.genre, "None")
        self.assertEqual(song3.genre, "None")
        self.assertEqual(song4.genre, "None")
        self.assertEqual(song5.genre, "Rap")
        self.assertEqual(song6.genre, "Rap")
        self.assertEqual(song7.genre, "Rap")
    	#testing album
        self.assertEqual(song1.album, "No Album")
        self.assertEqual(song2.album, "No Album")
        self.assertEqual(song3.album, "No Album")
        self.assertEqual(song4.album, "No Album")
        self.assertEqual(song5.album, "No Album")
        self.assertEqual(song6.album, "The Life of Pablo")
        self.assertEqual(song7.album, "The Life of Pablo")
    	#testing track length
        self.assertEqual(song1.track_length, 0)
        self.assertEqual(song2.track_length, 0)
        self.assertEqual(song3.track_length, 0)
        self.assertEqual(song4.track_length, 0)
        self.assertEqual(song5.track_length, 0)
        self.assertEqual(song6.track_length, 0)
        self.assertEqual(song7.track_length, 1127625)

    def testMovieConstructor(self):
        movie1 = proj1.Movie()
        movie2 = proj1.Movie("The Nice Guys")
        movie3 = proj1.Movie("Suicide Squad", "DC")
        movie4 = proj1.Movie("Spiderman: Homecoming", "Marvel Studios", 2017)
        movie5 = proj1.Movie("Avengers: Civil War", "Marvel Studios", 2016, 220)
        movie6 = proj1.Movie("Batman vs Superman", "DC", 2016, 250, "PG-13")

        #testing title
        self.assertEqual(movie1.title, "No Title")
        self.assertEqual(movie2.title, "The Nice Guys")
        self.assertEqual(movie3.title, "Suicide Squad")
        self.assertEqual(movie4.title, "Spiderman: Homecoming")
        self.assertEqual(movie5.title, "Avengers: Civil War")
        self.assertEqual(movie6.title, "Batman vs Superman")
        #testing author
        self.assertEqual(movie1.author, "No Author")
        self.assertEqual(movie2.author, "No Author")
        self.assertEqual(movie3.author, "DC")
        self.assertEqual(movie4.author, "Marvel Studios")
        self.assertEqual(movie5.author, "Marvel Studios")
        self.assertEqual(movie6.author, "DC")
        #testing release_year
        self.assertEqual(movie1.release_year, 2018)
        self.assertEqual(movie2.release_year, 2018)
        self.assertEqual(movie3.release_year, 2018)
        self.assertEqual(movie4.release_year, 2017)
        self.assertEqual(movie5.release_year, 2016)
        self.assertEqual(movie6.release_year, 2016)
        #testing movie_length
        self.assertEqual(movie1.movie_length, 0)
        self.assertEqual(movie2.movie_length, 0)
        self.assertEqual(movie3.movie_length, 0)
        self.assertEqual(movie4.movie_length, 0)
        self.assertEqual(movie5.movie_length, 220)
        self.assertEqual(movie6.movie_length, 250)
        #testing rating
        self.assertEqual(movie1.rating, "PG")
        self.assertEqual(movie2.rating, "PG")
        self.assertEqual(movie3.rating, "PG")
        self.assertEqual(movie4.rating, "PG")
        self.assertEqual(movie5.rating, "PG")
        self.assertEqual(movie6.rating, "PG-13")

    def test_str(self):
        #Testing __str__ method of media
        m1 = proj1.Media()
        self.assertEqual(m1.__str__(), "No Title by No Author (2018)")
        m2 = proj1.Media("Paper Towns", "John Green", 2013)
        self.assertEqual(m2.__str__(), "Paper Towns by John Green (2013)")
        m3 = proj1.Media("Short Film", "Pixar")
        self.assertEqual(m3.__str__(), "Short Film by Pixar (2018)")
        #Testing __str__ method of Song

        #Testing __str__ method of Movie

    def test_len(self):
        #testing __len__ method of media
        media = proj1.Media()
        self.assertEqual(media.__len__(), 0)
        #Testing __len__ method of Song
        song = proj1.Song()
        self.assertEqual(song.__len__(), 0)
        song2 = proj1.Song(track_length = 1000)
        self.assertEqual(song2.__len__(), 1000)
        #Testing __len__ method of Movie
        movie = proj1.Movie()
        self.assertEqual(movie.__len__(), 0)
        movie2 = proj1.Movie(movie_length = 134000)
        self.assertEqual(movie2.__len__(), 134000)

    def test_movie_has_no_genre(self):
        movie = proj1.Movie()
        self.assertTrue(not isinstance(movie, proj1.Song))

    def test_song_has_no_movie_length(self):
        song = proj1.Song()
        self.assertTrue(not isinstance(song, proj1.Movie))

    def test_media_song_has_no_rating(self):
        media = proj1.Media()
        self.assertTrue(not isinstance(media, proj1.Movie))

# ------------ TESTS FOR PART 2 ------------
    

    def test_json_Media(self):
        JSON_FILENAME = "sample_json.txt"
        f = open(JSON_FILENAME, 'r')
        dics = []
        i = 0
        for dic in f:
            dics.append(json.loads(dic))
            #print(dics[i], end = "\n\n\n\n\n\n\n\n")
            i += 1
        request = dics[-1]
        m1 = proj1.Media(json = request)
        f.close()
        
        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.release_year, '2012')
        self.assertEqual(m1.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(m1.__len__(), 0)

    def test_json_Song(self):
        JSON_FILENAME = "sample_json.txt"
        f = open(JSON_FILENAME, 'r')
        dics = []
        i = 0
        for dic in f:
            dics.append(json.loads(dic))
            #print(dics[i], end = "\n\n\n\n\n\n\n\n")
            i += 1
        request = dics[-2]
        s1 = proj1.Song(json = request)
        f.close()

        self.assertEqual(s1.title,"Hey Jude")
        self.assertEqual(s1.track_length, 431.333)
        self.assertEqual(s1.album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(s1.genre, "Rock")
        self.assertEqual(s1.__len__(), 431.333)
        self.assertEqual(s1.__str__(), "Hey Jude by The Beatles (1968)[Rock]")

    def test_json_Movie(self):
        JSON_FILENAME = "sample_json.txt"
        f = open(JSON_FILENAME, 'r')
        dics = []
        i = 0
        for dic in f:
            dics.append(json.loads(dic))
            #print(dics[i], end = "\n\n\n\n\n\n\n\n")
            i += 1
        request = dics[-3]
        movie1 = proj1.Movie(json = request)
        f.close()

        self.assertEqual(movie1.rating,"PG")
        self.assertEqual(movie1.release_year, '1975')
        self.assertEqual(movie1.movie_length, 124)
        self.assertEqual(movie1.__len__(), 124)
        self.assertEqual(movie1.__str__(), "Jaws by Steven Spielberg (1975)[PG]")

# ------------ TESTS FOR PART 3 ------------

    def test_nonsense(self):
        user_query = ""
        movies = []
        songs = []
        other_media = []
    
        base_url = "https://itunes.apple.com/search?term="
        user_query = user_query.replace(" ", "+")
        full_url = base_url + user_query
        itunes_result = requests.get(full_url)
        itunes_object = json.loads(itunes_result.text)
        for result in itunes_object["results"]:
            if "kind" in result:
                if result["kind"] == "song":
                    songs.append(proj1.Song(json = result))
                elif result["kind"] == "feature-movie":
                    movies.append(proj1.Movie(json = result))
                else:
                    other_media.append(proj1.Media(json = result))
            else:
                other_media.append(proj1.Media(json = result))
        self.assertTrue(movies == [])
        self.assertTrue(songs == [])
        self.assertTrue(songs == [])

        user_query = "*&^%()"
        movies = []
        songs = []
        other_media = []
    
        base_url = "https://itunes.apple.com/search?term="
        user_query = user_query.replace(" ", "+")
        full_url = base_url + user_query
        itunes_result = requests.get(full_url)
        itunes_object = json.loads(itunes_result.text)
        for result in itunes_object["results"]:
            if "kind" in result:
                if result["kind"] == "song":
                    songs.append(proj1.Song(json = result))
                elif result["kind"] == "feature-movie":
                    movies.append(proj1.Movie(json = result))
                else:
                    other_media.append(proj1.Media(json = result))
            else:
                other_media.append(proj1.Media(json = result))
        self.assertTrue(movies != [])
        self.assertTrue(songs != [])
        self.assertTrue(songs != [])

    def test_specifics(self):
        user_query = "Moana"
        movies = []
        songs = []
        other_media = []
    
        base_url = "https://itunes.apple.com/search?term="
        user_query = user_query.replace(" ", "+")
        full_url = base_url + user_query
        itunes_result = requests.get(full_url)
        itunes_object = json.loads(itunes_result.text)
        for result in itunes_object["results"]:
            if "kind" in result:
                if result["kind"] == "song":
                    songs.append(proj1.Song(json = result))
                elif result["kind"] == "feature-movie":
                    movies.append(proj1.Movie(json = result))
                else:
                    other_media.append(proj1.Media(json = result))
            else:
                other_media.append(proj1.Media(json = result))
        self.assertTrue(movies != [])
        self.assertTrue(songs != [])
        self.assertTrue(songs != [])

    def test_categories(self):
        user_query = "love"
        movies = []
        songs = []
        other_media = []
    
        base_url = "https://itunes.apple.com/search?term="
        user_query = user_query.replace(" ", "+")
        full_url = base_url + user_query
        itunes_result = requests.get(full_url)
        itunes_object = json.loads(itunes_result.text)
        for result in itunes_object["results"]:
            if "kind" in result:
                if result["kind"] == "song":
                    songs.append(proj1.Song(json = result))
                elif result["kind"] == "feature-movie":
                    movies.append(proj1.Movie(json = result))
                else:
                    other_media.append(proj1.Media(json = result))
            else:
                other_media.append(proj1.Media(json = result))
        self.assertTrue(movies != [])
        self.assertTrue(songs != [])
        self.assertTrue(songs != [])

        user_query = ""
        movies = []
        songs = []
        other_media = []
    
        base_url = "https://itunes.apple.com/search?term="
        user_query = user_query.replace(" ", "+")
        full_url = base_url + user_query
        itunes_result = requests.get(full_url)
        itunes_object = json.loads(itunes_result.text)
        for result in itunes_object["results"]:
            if "kind" in result:
                if result["kind"] == "song":
                    songs.append(proj1.Song(json = result))
                elif result["kind"] == "feature-movie":
                    movies.append(proj1.Movie(json = result))
                else:
                    other_media.append(proj1.Media(json = result))
            else:
                other_media.append(proj1.Media(json = result))
        self.assertTrue(movies == [])
        self.assertTrue(songs == [])
        self.assertTrue(songs == [])


unittest.main()
