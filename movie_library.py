import random
import datetime

class Movie ():
    def __init__(self, title, release, genre):
        self._title = title
        self._release = release
        self._genre = genre
        self._play_counter = 0

    def __str__(self):
        return f'{self._title} {self.release} {self.genre} {self._play_counter}'

    @property
    def title(self):
        return self._title
       
    @property
    def release(self):
        return self._release

    @property
    def genre(self):
        return self._genre    
    
    @property
    def play_counter(self):
        return self._play_counter

    @play_counter.setter
    def play_counter (self, number):
        self._play_counter = number
    
    def play(self):
        self._play_counter += 1
        print(f'You have watched {self._title} ({self.release})')

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._season = season
        self._episode = episode

    def __str__(self):
        return f'{self._title} {self.release} {self.genre} {self.season}{self.episode} {self._play_counter}'

    @property
    def season(self):
        return self._season

    @property
    def episode(self):
        return self._episode

    def play(self):
        self._play_counter += 1
        print(f'You have watched {self._title} {self.season}{self.episode}')


class Library ():
    def __init__(self):
        self._list = []
    
    @property
    def list(self):
        return self._list

    def add(self, object):
        if not (type(object) == Movie or type(object) == Series): 
            raise ValueError("neither a Movie nor Series")
        self._list.append(object)

    def create_seasons (self, title, release, genre, season, how_many_episodes):
        new_season = []
        for i in range (1,how_many_episodes+1):
            new_season.append(Series(title = title, release = release, genre = genre, season = f'S{season:02}', episode = f'E{i:02}'))
        for i in new_season:
            self.list.append(i)

    def get_movies(self):        
        return sorted([i for i in self.list if type(i) == Movie], key = lambda x: x.title)

    def get_series(self):
        return sorted([i for i in self.list if type(i) == Series], key = lambda x: x.title)

    
    def search(self, title):
        found = []
        for item in self.list:
            if item.title == title:
                found.append(item)
        if len(found) == 0:
            print(f'{title} not found')
        for i in found:
            print(i)

    def generate_views(self):
        chosen_item = random.choice(self.list)
        new_count = chosen_item.play_counter + random.randint(1, 100)
        chosen_item.play_counter=new_count
        return chosen_item.title, chosen_item.play_counter

    def generate_views_10x(self):
        x = []
        for i in range (10):
            a = self.generate_views()
            x.append(a)
        return x

    def top_titles (self, content_type, number):
        
        top = sorted(self.list, key = lambda x: x.play_counter, reverse=True)
        the_best = top[0:number]
        
        if content_type == "movie":
            top_m = []
            for movie in top:
                if type(movie) == Movie:
                    top_m.append(movie)
            the_best_m = top_m[0:number]
            return the_best, the_best_m

        elif content_type == "series":
            top_s = []
            for series in top:
                if type(series) == Series:
                    top_s.append(series)
            the_best_s = top_s[0:number]
            return the_best, the_best_s
            
        
        else:
            raise ValueError("neither a movie nor series")
        

real = [
Movie(title = 'Tie Me Up! Tie Me Down!', release = 1990, genre = 'Comedy'),
Movie(title = 'High Heels', release = 1991, genre = 'Comedy'),
Movie(title = 'Dead Zone  The', release = 1983, genre = 'Horror'),
Movie(title = 'Cuba', release = 1979, genre = 'Action'),
Movie(title = 'Days of Heaven', release = 1978, genre = 'Drama' ),
Movie(title = 'Octopussy', release = 1983, genre = 'Action' ),
Movie(title = 'Target Eagle', release = 1984, genre = 'Action' ),
Movie(title = 'American Angels: Baptism of Blood  The', release = 1989, genre = 'Drama' ),
Movie(title = 'Subway', release = 1985, genre = 'Drama' ),
Movie(title = 'Camille Claudel', release = 1990, genre = 'Drama' ),
Movie(title = 'Fanny and Alexander', release = 1982, genre = 'Drama' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S01', episode = 'E02' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S01', episode = 'E03' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E01' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E02' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E03' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E01' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E02' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E03' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E01' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E02' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E03' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E01' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E02' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E03' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E01' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E02' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E03' )
]

def go():
    
    print("Movie library")
    
    m = Movie(title = 'Tie Me Up! Tie Me Down!', release = 1990, genre = 'Comedy')
    s = Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E01' )
    
    print(f'''
    1. The library stores information about movies. Each instance should have the following attributes:
    title = {m.title}
    release = {m.release}
    genre = {m.genre}''')
    
    print(f'''
    2. The library stores information about series. Each instance should have the following attributes:
    title = {s.title}
    release = {s.release}
    genre = {s.genre}
    season ={s.season}
    episode = {s.episode}
    ''')


    print(f"""
    3. Movies and series have a play method that increases the number of plays of the title by 1.
    After viewing, information about the watched movie or episode is displayed.
    """)
    
    Series.play(s)
    Movie.play(m)

    print(f"""
    4. The library stores information in a list:
    """)
    
    Hani = Library()
    for i in real:
        Hani.add(i)
    
    print(Hani.list)
    
    print(f'''
    5. There is a method "create_seasons()" that adds full series seasons to the library.
    ''')
    
    title = "Mentalista"
    release = 2008
    genre = "crime" 
    season = 1
    how_many_episodes = 25

    Hani.create_seasons (title, release, genre,season,how_many_episodes)

    Hani.search("Mentalista")
    
    print(f'''
    6. There are methods: "get_movies()" and "get_series()" that filter the list and return only movies or series. The result is sorted alphabetically.''')

    only_movies = Hani.get_movies()
    only_series = Hani.get_series()
    
    print (f'''
    Only movies:

    ''')
    for i in only_movies:
        print (i)
    print (f'''
    Only series:
    ''')
    for i in only_series:
        print (i)

    print(f"""
    7. There is a method "search()" that searches for a movie or series by its title.
    """)

    Hani.search("Office")
    print ('')

    Hani.search("Hobbit")

    print(f'''
    8. There is a method "generate_views()" that randomly selects an item from the library and then adds a random (between 1 and 100) view number to it.
    There is also a method "generate_views_10x" which activates "generate_views" ten times.
    ''')

    gv = Hani.generate_views()
    print(f'''
    The result of activating "generate_views":
    
    {gv}
    ''')

    gv_10x = Hani.generate_views_10x()
    print(f'''
    The result of activating "generate_views_10x":
    
    {gv_10x}
    ''')

    print(f"""
    9.There is a method "top_titles()" that will return a selected amount of the most popular titles from the library. That can be display by movies or series , or all together.""")


    x = datetime.datetime.now().strftime("%d.%m.%Y")

    top3, top3m = Hani.top_titles("movie", 3)
    top3, top3s  = Hani.top_titles("series", 3)

    print(f'''
    most watched movies and series till {x}:
    ''')
    for i in top3:
        print(i)
    
    print(f'''
    most watched movies till {x}:
    ''')
    for i in top3m:
        print(i)
    
    print(f'''
    most watched series till {x}:
    ''')
    for i in top3s:
        print(i)
    

if __name__ == "__main__":
    go()