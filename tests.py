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

    def test_set_book_genre_existent_genre_true(self):
        collector = BooksCollector()

        collector.add_new_book('Фантомас')
        collector.set_book_genre('Фантомас', 'Ужасы')
        assert collector.get_book_genre('Фантомас') == 'Ужасы'

    @pytest.mark.parametrize('name',
                             ['Гарри поттер и узник азкабана sample_text sample_text ', ''])
    def test_add_new_book_name_more_than_41_symbol_and_equal_zero_false(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name',
                             ['Гарри поттер и узник азкабана sample_tex', '1'])
    def test_add_new_book_name_equal_40_symbols_and_equal_1_symbol_true(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    def test_get_book_genre_book_has_no_genre_true(self):
        collector = BooksCollector()

        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    def test_get_books_with_specific_genre_fantastic_one_book_true(self):
        collector = BooksCollector()
        book = 'Гарри Поттер'

        collector.add_new_book(book)
        collector.set_book_genre(book, 'Фантастика')
        assert book in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_for_children_one_books_in_list_true(self):
        collector = BooksCollector()

        collector.add_new_book('Вверх!')
        collector.set_book_genre('Вверх!', 'Мультфильмы')
        assert len(collector.get_books_for_children()) == 1 and collector.get_book_genre('Вверх!') == 'Мультфильмы'

    def test_add_book_in_favorites_sherlock_holmes_added_to_favourites_true(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс']

    def test_delete_book_from_favorites_one_book_deleted_true(self):
        collector = BooksCollector()

        collector.add_new_book('Вверх!')
        collector.add_book_in_favorites('Вверх!')
        collector.delete_book_from_favorites('Вверх!')
        assert len(collector.get_list_of_favorites_books()) == 0
