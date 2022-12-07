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

# TODO: Add your code to tasks 1 to 5 in this file.

class Book:
    """
    This class represents all information for a given book and is the overall parent class of the code.
    """
    FICTION: str = 'Fiction'
    NON_FICTION: str = 'Non Fiction'
    recommended: bool = False

    def __init__(self, title: str, author: str, rating: float, reviews: int, price: float, years: List[int], genre: str) -> None:
        """
        This method initializes the parameters of the class with the standard __init__ method.
        :param title: this is the name of the book as a string.
        :param author: this is the writer of the book as a string.
        :param rating: this is the rating out of 5 for the book to determine how much people liked it as a float.
        :param reviews: this is the number of total reviews a given book has as an integer.
        :param price: this is the amount that each book costs to buy as a float.
        :param years: this is a List of integers where if a given book has multiple years, this is where all the years are as integers.
        :param genre: this is the type of book which any given title has as a string.
        :return: This method returns nothing
        """
        self.title: str = title
        self.author: str = author
        self.rating: float = rating
        self.reviews: int= reviews
        self.price: float = price
        self.years: List[int] = years
        self.genre: str = genre


    def __str__(self) -> str:
        """
        This method is the string method.
        :return: This method returns the title of a given book from the csv file.
        """
        return f"{self.title}"

    def recommend(self, rating: float, n_reviews: int) -> None:
        """
        This method takes rating and n_reviews as self initializing parameters, it just compares the ratings and reviews to find the highest value.
        :param rating: initialized as the integer = 0.
        :param n_reviews: initialized as the integer = 0.
        :return: This method returns nothing.
        """
        if rating <= self.rating and n_reviews <= self.reviews:
            self.recommended: bool = True
        else:
            self.recommended: bool = False

class Amazon:
    """
    This class represents the bestseller books for any given year.
    """
    def __init__(self, bestsellers: List[Book]) -> None:
        """
        This method initializes the needed parameters.
        :param bestsellers: This is a list of the Books (bestsellers) which is taken from the bestsellers.
        :return: thid method returns nothing.
        """
        self.bestsellers: List[Book] = bestsellers

    def read_books_csv(self, path: str) -> None:
        """
        This method seperates the fiction and non fiction books in the bestsellers list.
        :param path: This takes the path of the file
        :return: This method returns nothing
        """
        data: Dict = {}
        with open(path, 'r', encoding='utf-8-sig') as file:
            data_csv = csv.reader(file)
            next(data_csv)
            for row in data_csv:
                title: str = row[0]
                author: str = row[1]
                user_rating: float = float(row[2])
                reviews: int = int(row[3])
                price: float = float(row[4])
                year: int = int(row[5])
                genre: str = row[6]

                if title not in data:
                    data[title] = {'author': author, 'user_rating': user_rating, 'reviews': reviews,
                                   'price': price, 'years': [year], 'genre': genre}
                else:
                    data[title]['years'].append(year)

        for title in data:
            current_book: Dict = data[title]
            if current_book['genre'] == Book.FICTION:
                book = FictionBook(title, current_book['author'], current_book['user_rating'],
                                   current_book['reviews'], current_book['price'],
                                   current_book['years'])

            else:
                book = NonFictionBook(title, current_book['author'], current_book['user_rating'],
                                      current_book['reviews'], current_book['price'],
                                      current_book['years'])
            self.bestsellers.append(book)

    def best_year_rating(self) -> int:
        """

        :return:
        """
        years_ratings: Dict = {}
        for year in range(2009, 2020):
            for book in self.bestsellers:
                if year in book.years:
                    if year not in years_ratings:
                        years_ratings[year] = [book.rating]
                    else:
                        years_ratings[year].append(book.rating)

        max_med: float = statistics.median(list(years_ratings.values())[-1])
        max_year: int = list(years_ratings.keys())[-1]
        for year in years_ratings:
            curr_median: float = statistics.median(years_ratings[year])

            if curr_median > max_med:
                max_med: float = curr_median
                max_year: int = year

        return max_year

    def best_year_reviews(self) -> int:
        """

        :return:
        """
        years_reviews: Dict = {}
        for year in range(2009, 2020):
            for book in self.bestsellers:
                if year in book.years:
                    if year not in years_reviews:
                        years_reviews[year] = [book.reviews]
                    else:
                        years_reviews[year].append(book.reviews)

        max_med: float = statistics.median(list(years_reviews.values())[-1])
        max_year: int = list(years_reviews.keys())[-1]

        for year in years_reviews:
            curr_median: float = statistics.median(years_reviews[year])

            if curr_median > max_med:
                max_med: float = curr_median
                max_year: int = year

        return max_year

    def recommend_book(self, rating: float, n_reviews: int) -> None:
        """

        :param rating:
        :param n_reviews:
        :return:
        """
        for book in self.bestsellers:
            book.recommend(rating, n_reviews)

    def get_recommendations(self) ->List[str]:
        """

        :return:
        """
        recommended_books: list = []
        for book in self.bestsellers:
            if book.recommended == True:
                recommended_books.append(str(book))
        return recommended_books

class FictionBook(Book):
    """

    """

    def __init__(self, title: str, author: str, rating: float, reviews: int, price: float, years: List[int]) -> None:
        """

        :param title:
        :param author:
        :param rating:
        :param reviews:
        :param price:
        :param years:
        """
        super().__init__(title, author, rating, reviews, price, years, Book.FICTION)

    def __str__(self) -> str:
        """

        :return:
        """
        # Use .join method for the next line
        return f"{self.title}: {self.genre} ({self.years[0]})"

class NonFictionBook(Book):
    """

    """

    def __init__(self, title: str, author: str, rating: float, reviews: int, price: float, years: List[int]) -> None:
        """

        :param title:
        :param author:
        :param rating:
        :param reviews:
        :param price:
        :param years:
        """
        super().__init__(title, author, rating, reviews, price, years, Book.NON_FICTION)

    def __str__(self) -> str:
        """

        :return:
        """
        # Use .join method for the next line
        return f"{self.title}: {self.genre} ({self.years[0]})"