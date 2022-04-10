from unittest.mock import MagicMock
import pytest
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='title1', description='description1', trailer='trailer1', year=1990, rating=3, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='title2', description='description2', trailer='trailer2', year=1999, rating=5, genre_id=1, director_id=1)
    movie_3 = Movie(id=3, title='title3', description='description3', trailer='trailer3', year=2000, rating=1, genre_id=1, director_id=1)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMoviesService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'description': 'Test',
            'rating': 6,
            'title': 'Test',
            'trailer': 'Test',
            'year': 2000,
            'genre_id': 18,
            'director_id': 1
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        result = self.movie_service.delete(1)
        assert result is None

    def test_update(self):
        movie_d = {
            'id': 4,
            'description': 'Test2',
            'rating': 6,
            'title': 'Test2',
            'trailer': 'Test2',
            'year': 2000,
            'genre_id': 18,
            'director_id': 1
        }
        result = self.movie_service.update(movie_d)
        assert result != None
