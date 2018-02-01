import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

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

    	#testing album

    	#testing track length


unittest.main()
