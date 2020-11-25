class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __print__(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


t = input()
a = input()
y = input()
painting = Painting(t, a, y)
painting.__print__()
