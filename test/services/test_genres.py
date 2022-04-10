from unittest.mock import MagicMock
import pytest
from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='name1')
    genre_2 = Genre(id=2, name='name2')
    genre_3 = Genre(id=3, name='name3')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenresService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None


    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            'name': 'name4'
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_delete(self):
        result = self.genre_service.delete(1)
        assert result is None

    def test_update(self):
        genre_d = {
            'id': 3,
            'name': 'update_name'
        }
        result = self.genre_service.update(genre_d)
        assert result != None