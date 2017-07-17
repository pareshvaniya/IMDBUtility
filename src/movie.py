import imdb

class Movie(object):
    def __init__(self, title, year):
        self.title = title
        self.year = year
    
    def __str__(self):
        return '%s (%s)' % (self.title, self.year)
    
    def __eq__(self, other):
        if type(other) != Movie: return False
        return other.title == self.title and other.year == self.year
    
    @staticmethod
    def create_movie_from_imdb_query(query):
        db = imdb.IMDb()
        #movie_obj = db.search_movie(query, results=1)[0]
        #created_movie = Movie(title=movie_obj['title'], year=movie_obj['year'])
        return query
