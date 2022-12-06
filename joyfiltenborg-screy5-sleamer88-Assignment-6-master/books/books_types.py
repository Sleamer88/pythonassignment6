"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

from typing import Dict, List
import csv
import statistics
"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

from typing import Dict, List
import csv
import statistics

class Book:
    """
    This class represents all information for a given book.
    """
    FICTION = 'Fiction'
    NON_FICTION = 'Non Fiction'
    recommended: bool = False

    def __init__(self, title: str, author: str, rating: float, reviews: int, price: float, years: List[int], genre: str) -> None:
        self.title = title
        self.author = author
        self.rating = rating
        self.reviews = reviews
        self.price = price
        self.years = years
        self.genre = genre


    def __str__(self) -> str:
        return f"{self.title}"

    def recommend(self, rating, n_reviews):
        if Book.FICTION == 'Fiction': #or Book.NON_FICTION == "Non Fiction":
            if rating <= self.rating and n_reviews < self.reviews:
                self.recommended = True

            # if rating < self.rating and n_reviews > self.reviews:
            #     self.recommended = True

class Amazon:
    """
    This class represents the bestseller books.
    """
    def __init__(self, bestsellers: List[Book]):
        self.bestsellers = bestsellers

    def read_books_csv(self, path: str) -> None:
        data = {}
        with open(path, 'r', encoding='utf-8-sig') as file:
            data_csv = csv.reader(file)
            next(data_csv)
            for row in data_csv:
                title = row[0]
                author = row[1]
                user_rating = float(row[2])
                reviews = int(row[3])
                price = float(row[4])
                year = int(row[5])
                genre = row[6]

                if title not in data:
                    data[title] = {'author': author, 'user_rating': user_rating, 'reviews': reviews,
                                   'price': price, 'years': [year], 'genre': genre}
                else:
                    data[title]['years'].append(year)

        for title in data:
            current_book = data[title]
            if current_book['genre'] == 'Fiction':
                book = FictionBook(title, current_book['author'], current_book['user_rating'],
                                   current_book['reviews'], current_book['price'],
                                   current_book['years'])

            else:
                book = NonFictionBook(title, current_book['author'], current_book['user_rating'],
                                      current_book['reviews'], current_book['price'],
                                      current_book['years'])
            self.bestsellers.append(book)

    def best_year_rating(self):
        years_ratings = {}
        for year in range(2009, 2020):
            for book in self.bestsellers:
                if year in book.years:
                    if year not in years_ratings:
                        years_ratings[year] = [book.rating]
                    else:
                        years_ratings[year].append(book.rating)

        max_med = statistics.median(list(years_ratings.values())[-1])
        max_year = list(years_ratings.keys())[-1]
        for year in years_ratings:
            curr_median = statistics.median(years_ratings[year])

            if curr_median > max_med:
                max_med = curr_median
                max_year = year

        return max_year

    def best_year_reviews(self):
        years_reviews = {}
        for year in range(2009, 2020):
            for book in self.bestsellers:
                if year in book.years:
                    if year not in years_reviews:
                        years_reviews[year] = [book.reviews]
                    else:
                        years_reviews[year].append(book.reviews)

        max_med = statistics.median(list(years_reviews.values())[-1])
        max_year = list(years_reviews.keys())[-1]

        for year in years_reviews:
            curr_median = statistics.median(years_reviews[year])

            if curr_median > max_med:
                max_med = curr_median
                max_year = year

        return max_year

    def recommend_book(self, rating, n_reviews):
        for book in self.bestsellers:
            book.recommend(rating, n_reviews)

    def get_recommendations(self):
        recommended_books = []
        for book in self.bestsellers:
            if book.recommended == True:
                recommended_books.append(str(book))
        return recommended_books

class FictionBook(Book):

    def __init__(self, title: str, author: str, rating: float, reviews: int, price: float, years: List[int]):
        super().__init__(title, author, rating, reviews, price, years, Book.FICTION)

    def __str__(self):
        # Use .join method for the net line
        return f"{self.title}: {self.genre} ({self.years[0]})"

class NonFictionBook(Book):

    def __init__(self, title: str, author: str, rating: float, reviews: int, price: float, years: List[int]):
        super().__init__(title, author, rating, reviews, price, years, Book.NON_FICTION)

    def __str__(self):
        # Use .join method for the next line
        return f"{self.title}: {self.genre} ({self.years[0]})"

# TODO: Add your code to tasks 1 to 5 in this file.


# b = Amazon([])
# b.read_books_csv('/Users/robbie/PycharmProjects/pythonassignment6/joyfiltenborg-screy5-sleamer88-Assignment-6-master')
# print(b.bestsellers[0])
# print(b.best_year_rating())
# print(b.best_year_reviews())
# b.recommend_book(4.8, 5000)
# print(len(b.get_recommendations()))
# TODO: Add your code to tasks 1 to 5 in this file.

