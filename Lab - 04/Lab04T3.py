class Item:
    def viewFullDescription(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price}")
    def addToShoppingBasket(self):
        print(f"{self.name} has been added to the shopping basket.")
    def removeFromShoppingBasket(self):
        print(f"{self.name} has been removed from the shopping basket.")
class MP3(Item):
    def play(self):
        print(f"Playing {self.name} by {self.artist}.")
    def download(self):
        print(f"Downloading {self.name}...")
class DVD(Item):
    def viewTrailer(self):
        print(f"Viewing trailer for {self.name}.")
class Book(Item):
    def previewContent(self):
        print(f"Previewing content from the book {self.name} by {self.author}.")
print("============================================================")
mp3_2 = MP3()
mp3_2.name = "Regrets"
mp3_2.description = "Emotional rap song with deep lyrics"
mp3_2.price = 200
mp3_2.artist = "Talha Anjum"
mp3_2.duration = "3:45"
mp3_2.viewFullDescription()
mp3_2.play()
mp3_2.addToShoppingBasket()
print("============================================================")
dvd = DVD()
dvd.name = "Peaky Blinders"
dvd.description = "British crime drama series set after World War I"
dvd.price = 2000
dvd.certificate = "18+"
dvd.duration = "6 Seasons"
dvd.actors = ["Cillian Murphy", "Tom Hardy", "Paul Anderson"]
dvd.viewFullDescription()
dvd.viewTrailer()
print("============================================================")
book = Book()
book.name = "Peer-e-Kamil"
book.description = "A spiritual and emotional novel"
book.price = 600
book.author = "Umera Ahmed"
book.numberOfPages = 450
book.genre = "Spiritual Fiction"
book.viewFullDescription()
book.previewContent()
print("============================================================")