import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # параметризованный метод тут должен быть
    @pytest.mark.parametrize('name,genre', [['Гарри Поттер', 'Фантастика'], ['Гордость и предубеждение и зомби', 'Ужасы'], ['Шерлок Холмс', 'Детективы'], ['Вверх!', 'Мультфильмы'], ['Ревизор', 'Комедии']])
    def test_set_book_genre_existent_genre_true(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_add_new_book_add_name_more_than_41_symbol_false(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить???')
        assert len(collector.get_books_genre()) == 0

    def test_get_book_genre_harry_potter_is_fantastic_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_book_has_no_genre_true(self):
        collector = BooksCollector()

        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    def test_get_books_with_specific_genre_fantastic_2_books_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Мстители')
        collector.set_book_genre('Мстители', 'Фантастика')
        collector.add_new_book('Агент 007')
        collector.set_book_genre('Агент 007', 'Боевик')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_genre_five_books_in_list_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_new_book('Вверх!')
        collector.set_book_genre('Вверх!', 'Мультфильмы')
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        assert len(collector.get_books_genre()) == 5

    def test_get_books_for_children_three_books_in_list_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_new_book('Вверх!')
        collector.set_book_genre('Вверх!', 'Мультфильмы')
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        assert len(collector.get_books_for_children()) == 3
        assert 'Гордость и предубеждение и зомби' and 'Шерлок Холмс' not in collector.get_books_for_children()

    def test_add_book_in_favorites_sherlock_holmes_and_up_added_to_favourites_true(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_new_book('Вверх!')
        collector.add_book_in_favorites('Вверх!')
        assert collector.favorites == ['Шерлок Холмс', 'Вверх!']

    def test_delete_book_from_favorites_up_was_deleted_true(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_new_book('Вверх!')
        collector.add_book_in_favorites('Вверх!')
        collector.delete_book_from_favorites('Вверх!')
        assert collector.favorites == ['Шерлок Холмс']

    def test_get_list_of_favorites_books_sherlock_holmes_and_auditor_in_list_true(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс', 'Ревизор']
