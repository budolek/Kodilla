import random
from faker import Faker
from datetime import date

fake = Faker("pl_PL")

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        
    def genres(self, genre):
        self.genre = genre
        
    def play(self, views): 
        views += 1
        self.views = views
        
    def __str__(self):
        return f"{self.title.title()} | Gatunek: {self.genre} | Rok wydania: {self.year} | Oglądalność: {self.views}"
    
class Serials(Movie):
    def __init__(self, se_num, ep_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.se_num = se_num
        self.ep_num = ep_num
        
    @property
    def ep_all(self):
        allep = random.randrange(8, 14, 2)
        self.allep = allep
        return self.allep * self.se_num 
    
    def __str__(self):
        return f"{self.title.title()} | Gatunek: {self.genre} | Odcinek: S{self.se_num:02}E{self.ep_num:02} | Oglądalność: {self.views}"
    
vid_lib = [] 

def how_many(func):
    def multiple():
        for i in range(10):
            func()
    return multiple()

@how_many
def add_libry():
        vid_lib.append(Movie(title = fake.word(), year = fake.year()))
        vid_lib.append(Serials(title = fake.word(), year = fake.year(), se_num = fake.random_digit_not_null(), ep_num = fake.random_int(1, 14)))

for x in vid_lib:
    views = 0
    x.play(views)
    genre = ["Komedia", "Thriller", "Dramat", "Akcja", "Biograficzny", "Horror"]
    x.genres(random.choice(genre))
    
@how_many
def generate_views():
    random.shuffle(vid_lib)
    vid_lib[0].views += random.randrange(1, 100)

def get_series():
    series = []
    for i in vid_lib:
        if i.__class__.__name__ == "Serials":
            series.append(i)
    return sorted(series, key=lambda serials: serials.title)

def get_movies():
    movies = []
    for i in vid_lib:
        if i.__class__.__name__ == "Movie":
            movies.append(i) 
    return sorted(movies, key=lambda movie: movie.title)

def search(x):
    for i in range(len(vid_lib)):
        if vid_lib[i] == x:
            print(f"\nWynik wyszukiwania dla: '{x.title.title()}'", x, sep = '\n')

def top_titles(num):
    vid_lib[:] = sorted(vid_lib, key = lambda video: video.views, reverse=True)
    print(f"\nNajpopularniejsze filmy i seriale dnia {date.today():%d.%m.%Y}:\n")
    print(*vid_lib[:num], sep = '\n')

seriale = get_series()
filmy = get_movies()
   
    
print("\nBiblioteka filmów\n")
generate_views(10)
print("Filmy\n")
for i in filmy:
    print(i)
print("\nSeriale\n")
for i in seriale:
    print(i)
top_titles(3)
search(x)










