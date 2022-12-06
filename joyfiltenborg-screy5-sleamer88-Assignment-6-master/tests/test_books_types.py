# -*- coding: utf-8 -*-

"""
XB_0082: Bestselling Books

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

import pytest
from books.books_types import *
from books.books_utils import *
from typing import Dict, List


# Testing data
book = Book('Catching Fire (The Hunger Games)', 'Suzanne Collins', 4.7, 22614, 11, [2010], 'Fiction')
fiction = FictionBook('Catching Fire (The Hunger Games)', 'Suzanne Collins', 4.7, 22614, 11, [2010])
nonfiction = NonFictionBook('Calm the F*ck Down: An Irreverent Adult Coloring Book (Irreverent Book Series)', "Sasha O'Hara", 4.6, 10369, 4, [2016])


@pytest.fixture
def singleton() -> Amazon:
    path = get_absolute_path('data/books.csv')
    amazon = Amazon([])
    amazon.read_books_csv(path)
    return amazon


@pytest.fixture
def bestsellers() -> Dict[int, List[str]]:
    path = get_absolute_path('data/books.csv')
    bestsellers = {
        Book.FICTION: [],
        Book.NON_FICTION: []
    }

    with open(path, encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        temporary = []
        for row in reader:
            genre = row['Genre']
            title = row['Name']

            if title not in temporary:
                temporary += [title]
                if genre == 'Fiction':
                    bestsellers[Book.FICTION] += [title]
                else:
                    bestsellers[Book.NON_FICTION] += [title]

    return bestsellers



# -----------------------------------------
# Task 1
# -----------------------------------------

def test_book():
    created = True
    try:
        Book('Catching Fire (The Hunger Games)', 'Suzanne Collins', 4.7, 22614, 11, 2010, 'Fiction')
    except:
        created = False

    msg = '[Task 1] Cannot create a Book object'
    assert created, msg


def test_book_attrs():
    attrs = ['title', 'author', 'rating', 'reviews', 'price', 'years', 'genre']

    for attr in attrs:
        msg = f'[Task 1] Book objects do not have the {attr} attribute'
        assert hasattr(book, attr), msg


def test_book_fiction_attr():
    result = 'FICTION' in dir(Book)

    if result:
        result = Book.FICTION == 'Fiction'

    msg = '[Task 1] The FICTION class attribute of the Book class was wrongly defined.'
    assert result, msg


def test_book_nonfiction_attr():
    result = 'NON_FICTION' in dir(Book)

    if result:
        result = Book.NON_FICTION == 'Non Fiction'

    msg = '[Task 1] The NON_FICTION class attribute of the Book class was wrongly defined.'
    assert result, msg


def test_book_str():
    expected = book.title
    output = str(book)
    msg = f'[Task 1] The Book __str__() method is incorrect. Expected: {expected} - Obtained: {output}'
    assert output.lower() == expected.lower(), msg


def test_amazon():
    created = True
    try:
        Amazon([])
    except:
        created = False

    msg = '[Task 1] Cannot create a Amazon object'
    assert created, msg


def test_amazon_attrs():
    amazon = Amazon([])
    result = hasattr(amazon, 'bestsellers')

    msg = '[Task 1] The Amazon object do not have the bestsellers attribute'
    assert result, msg


# -----------------------------------------
# Task 2
# -----------------------------------------

def test_fiction():
    created = True
    try:
        FictionBook('Catching Fire (The Hunger Games)', 'Suzanne Collins', 4.7, 22614, 11, [2010])
    except:
        created = False

    msg = '[Task 2] Cannot create a FictionBook object'
    assert created, msg


def test_nonfiction():
    created = True
    try:
        NonFictionBook('Calm the F*ck Down: An Irreverent Adult Coloring Book (Irreverent Book Series)',"Sasha O'Hara", 4.6, 10369, 4, 2016)
    except:
        created = False

    msg = '[Task 2] Cannot create a NonFictionBook object'
    assert created, msg


def test_fiction_subclass():
    result = issubclass(FictionBook, Book)
    msg = '[Task 2] FictionBook is not a subclass of Book'
    assert result, msg


def test_nonfiction_subclass():
    result = issubclass(NonFictionBook, Book)
    msg = '[Task 2] NonFictionBook is not a subclass of Book'
    assert result, msg


def test_fiction_attrs():
    attrs = ['title', 'author', 'rating', 'reviews', 'price', 'years', 'genre', 'recommended']
    result = True
    missing = None

    for attr in attrs:
        if not hasattr(fiction, attr):
            result = False
            missing = attr
            break

    msg = f'[Task 2] FictionBook objects do not have the {missing} attribute'
    assert result, msg


def test_nonfiction_attrs():
    attrs = ['title', 'author', 'rating', 'reviews', 'price', 'years', 'genre', 'recommended']
    result = True
    missing = None

    for attr in attrs:
        if not hasattr(nonfiction, attr):
            result = False
            missing = attr
            break

    msg = f'[Task 2] FictionBook objects do not have the {missing} attribute'
    assert result, msg


def test_fiction_genre():
    expected = Book.FICTION
    output = fiction.genre
    msg = f'[Task 2] The genre of FictionBook objects is incorrect. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg


def test_nonfiction_genre():
    expected = Book.NON_FICTION
    output = nonfiction.genre
    msg = f'[Task 2] The genre of NonFictionBook objects is incorrect. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg


def test_fiction_str():
    expected = 'Catching Fire (The Hunger Games): Fiction (2010)'
    output = str(fiction)
    msg = f'[Task 2] The FictionBook __str__() method is incorrect. Expected: {expected} - Obtained: {output}'
    assert output.lower() == expected.lower(), msg


def test_nonfiction_str():
    expected = f'{nonfiction.title}: Non Fiction (2016)'
    output = str(nonfiction)
    msg = f'[Task 2] The NonFictionBook __str__() method is incorrect. Expected: {expected} - Obtained: {output}'
    assert output.lower() == expected.lower(), msg


# -----------------------------------------
# Task 3
# -----------------------------------------

def test_list_of_bestsellers_length(singleton, bestsellers):
    expected = len(bestsellers[Book.FICTION]) + len(bestsellers[Book.NON_FICTION])
    output = len(singleton.bestsellers)
    msg = f'[Task 3] The number of books is incorret. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg


def test_fiction_length(singleton, bestsellers):
    expected = len(bestsellers[Book.FICTION])
    output = len([p for p in singleton.bestsellers if isinstance(p, FictionBook)])
    msg = f'[Task 3] The number of fiction books is incorret. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg


def test_nonfiction_length(singleton, bestsellers):
    expected = len(bestsellers[Book.NON_FICTION])
    output = len([p for p in singleton.bestsellers if isinstance(p, NonFictionBook)])
    msg = f'[Task 3] The number of non-fiction books is incorret. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg


def test_list_of_bestsellers_content(singleton, bestsellers):
    set_fiction = set(bestsellers[Book.FICTION])
    set_nonfiction = set(bestsellers[Book.NON_FICTION])
    expected = set_fiction | set_nonfiction

    output = set()

    for p in singleton.bestsellers:
        output.add(p.title)

    msg = f'[Task 3] The content of the Amazon books attribute does not match with expected output.'
    assert expected == output, msg


def test_replace_empty_str(singleton, bestsellers):
    for p in singleton.bestsellers:
        assert p.rating != '', f'[Task 3] The rating value of {p.rating} in an empty string'


# -----------------------------------------
# Task 4
# -----------------------------------------

def test_find_best_rating(singleton):
    expected = 2019
    output = singleton.best_year_rating()
    msg = f'[Task 4] The year with best ratings is incorrect. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg

def test_find_best_reviews(singleton):
    expected = 2019
    output = singleton.best_year_reviews()
    msg = f'[Task 4] The year with best reviews is incorrect. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg

# -----------------------------------------
# Task 5
# -----------------------------------------

def test_recommended_attr():
    msg = f'[Task 5] Book objects do not have the recommended attribute.'
    assert hasattr(book, 'recommended'), msg


def test_recommend_fiction():
    fiction.recommend(4.7, 22614)
    msg = f'[Task 5] The FictionBook has not been recommended when fulfilling all criteria.'
    assert fiction.recommended, msg


def test_recommend_fiction_rating():
    fiction.recommend(4.8, 22614)
    msg = f'[Task 5] The FictionBook has been recommended when it does not have the required rating.'
    assert not fiction.recommended, msg


def test_recommend_fiction_reviews():
    fiction.recommend(4.7, 22615)
    msg = f'[Task 5] The FictionBook has been recommended when it does not have the required reviews.'
    assert not fiction.recommended, msg


def test_recommend_nonfiction():
    nonfiction.recommend(4.6, 10369)
    msg = f'[Task 5] The NonFictionBook has not been recommended when fulfilling all criteria.'
    assert nonfiction.recommended, msg


def test_recommend_nonfiction_rating():
    nonfiction.recommend(4.7, 10369)
    msg = f'[Task 5] The NonFictionBook has been recommended when it does not have the required rating.'
    assert not nonfiction.recommended, msg


def test_recommend_nonfiction_reviews():
    nonfiction.recommend(4.6, 10370)
    msg = f'[Task 5] The NonFictionBook has been recommended when it does not have the required reviews.'
    assert not nonfiction.recommended, msg


def test_get_recommended_fiction(singleton):
    singleton.recommend_book(4.5, 5000)
    output = len(singleton.get_recommendations())
    expected = 177

    msg = f'[Task 5] The number of recommended fiction books is incorrect. Expected: {expected} - Obtained: {output}'
    assert output == expected, msg


def test_get_recommended_nonfiction(singleton):
    singleton.recommend_book(5, 5000)
    output = len(singleton.get_recommendations())
    expected = 0

    msg = f'[Task 5] The number of recommended non-fiction books is incorrect. Expected: {expected} - Obtained: {output}'
    assert output == expected, msg