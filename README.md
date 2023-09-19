# qa_python
Добавлены следующие тесты:
1) test_set_book_genre_existent_genre_true
Проверяет, что добавляются книги с существующими (разрешёнными) жанрами
2) test_add_new_book_add_name_more_than_41_symbol_false
Проверяет, что если имя добавляемой книги > 41 символа, то книга не добавляется
3) test_get_book_genre_harry_potter_is_fantastic_true
Проверяет, что жанр добавленной книги соответствует жанру из списка
4) test_get_book_genre_book_has_no_genre_true
Проверяет, что у добавленной книги нет жанра
5) test_get_books_with_specific_genre_fantastic_2_books_true
Проверяет, что в списке с определённым жанром содержатся 2 книги этого жанра
6) test_get_books_genre_five_books_in_list_true
Проверяет, что добавлено 5 книг определённого жанра из списка
7) test_get_books_for_children_three_books_in_list_true
Проверяет, что в списке книг для детей содержится 3 книги, а также 2 книги неподходящего жанра отсутствуют
8) test_add_book_in_favorites_sherlock_holmes_and_up_added_to_favourites_true
Проверяет, что в "Избранные" были успешно добавлены книги
9) test_delete_book_from_favorites_up_was_deleted_true
Проверяет, что из списка "Избранные" была успешно удалена книга
10) test_get_list_of_favorites_books_sherlock_holmes_and_auditor_in_list_true
Проверяет, что список "Избранные" содержит добавленные книги