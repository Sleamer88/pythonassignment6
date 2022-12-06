# XB_0082 - Assignment 6 (2022-2023)

-----
* **Group Number**: /replace by your group number on canvas/
* **Contributor 1**: /replace by your full name/
* **VUnet ID number 1**: /replace by your VUnet ID number/
* **Contributor 2**: /replace by your full name/
* **VUnet ID number 2**: /replace by your VUnet ID number/
  
**Date**: /replace by date of first modification/

-----

## Introduction

With a continuous increase in self-publishing, in 2019, an average of 2,700 books was published every day. Based simply on numbers, the competition for becoming a bestseller is fierce. 

In this assignment, we will focus on Amazon's Top 50 bestselling books from 2009 to 2019. We'll look into what books managed to be bestsellers in multiple years, what was the average rating per year, and the average number of reviews.

### The Amazon Bestsellers

A dataset of 550 books doesn't say much for the average person. As data engineers, we would like to analyze the dataset and create an accessible way of getting insight out of it. This assignment aims to test your knowledge of classes and to inspire your logical creativity. 

#### Dataset
The dataset consists of 50 Amazon Bestsellers for every year from 2009 to 2019, with a total of 550 books. You can find all the information on [Kaggle](https://www.kaggle.com), a famous website containing many datasets, challenging tasks, and tons of inspiration from other coders. For more information visit [this link](https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019).

Please note that our project  contains the `bestsellers with categories.csv` file, but it has been renamed as `books.csv`. Check out the website to find out what the data looks like! The dataset is stored as a CSV file, whose values are separated by commas. The first line of the CSV file contains the following headers:

| Column | Description | 
|:-------|:------------|
| `Name` | Name of the Book |
| `Author` | The author of the Book |
| `User rating` | Amazon User Rating |
| `Reviews` | Number of written reviews on amazon |
| `Price` | The price of the book (as of 13/10/2020) | 
| `Year` | The Year(s) it ranked on the bestseller |
| `Genre` | Whether fiction or non-fiction |
	

-----

## Grading

This assignment consists of 5 tasks. Each task accounts for a different percentage of the grade. The correct development of each task is automatically checked by a set of unit tests. The assignment will eventually be graded by a tutor. 

Make sure all functions have type hints and a docstring that describes their purpose. You must follow all coding conventions defined on the Python Coding Standard document available via Canvas, otherwise, points will be deducted from your grade.

-----

## Testing

Implementing every single task in this assignment is necessary for the code in main to run. To help you verify your work intermediately we have implemented some tests. See pytest.md for instructions how to use these tests.

Note that all passing unit tests does not mean that your assignment is perfect. However, failing tests means that your assignment contains errors, such as incomplete tasks or bad code.

-----

## Tasks
To start with the assignment, fill in the information related to the contributors' name, ID, and date, displayed at the beginning of this document:

```python
* Contributor 1: ...
* VUnet ID number 1: ...
* Contributor 2: ...
* VUnet ID number 2: ...
* Date: ...
```

To complete the program you will need to complete five tasks.
Each task must be developed within the `books_types.py` file.

### Task 0: GitHub (10%)

We want to ease the collaboration in a pair by creating issues on GitHub. To do so, go to your online Git repository and create at least one issue per task (for tasks 1, 2, 3, 4, and 5).

For tasks 1 to 5, you are requested to make some modifications to the code. To start `clone` the project to your computer. To let our partner know we did our job, you should `add`, `commit`, and `push` your changes frequently. To get your partner's changes, remember to `pull` them from the server. Both members of the pair should commit and push changes to the repository. Now, every time that you are done with an **issue** you must close it to track the progress of the project.

Your TA will show you how to do all these different steps. For more information about git take a look at the following resources:
- https://www.w3schools.com/git/default.asp?remote=github
- https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html

### Task 1: Create Amazon and Book Classes (10%)

- Create the `Book` class, which contains the `title` (string), `author` (string), `rating` (float), `reviews` (integer), `price` (float), `years` (list of integers), and `genre` (string) attributes. Don't forget to create its constructor with the corresponding parameters in the given order.
- Define the `__str__()` method in the `Book` class. The method should return the title of the book.
- Create the `Amazon` class, which represents the list of bestsellers and only contains the attribute `bestsellers` (list of Books). Don't forget to create its constructor with the corresponding parameter.

**Note** Use the tests to verify this task since the main program will not run.

### Task 2: Create FictionBook and NonFictionBook Classes (20%)

- Create the class attributes `FICTION` and `NON_FICTION` in the `Book` class. The former should be set to 'Fiction' and the latter to 'Non Fiction'. These should be used to set the `genre` parameter when creating a `Book` object.
- There are two types of books: fiction and non-fiction books. Create the classes `FictionBook` and `NonFictionBook`. Both of them should inherit from the `Book` class.
- Implement the `__init__()` methods of the `FictionBook` and `NonFictionBook` classes. Both get as parameters the `title` (string), `author` (string), `rating` (float), `reviews` (integer), `price` (float), and `years` (list of integers) values for the instance attributes. When calling the constructor of the parent class, use the corresponding `Book` class attribute to set the `genre` value.
- Change the `__str__()` method in both classes. The method should return the title of the book along with the genre and the year(s) in which it was a bestseller. The string should follow the structure "`title`: `genre` (`year1`, `year2`, ..., `yearN`)".


### Task 3: Create Books from Dataset (25%)

Create the method `read_books_csv()` in the `Amazon` class. 
The method takes a path to a file as input and returns nothing. 
The method should instead populate the `bestsellers` attribute with `Book` objects created from the dataset.
You should create either `FictionBook` or `NonFictionBook` objects, which will depend on the type of the book.
This time you must use the `csv` module to read the CSV file.
To open the file with the `open()` function, you need to set the `encoding` parameter to `'utf-8-sig'`.

*Additional remarks:*

- Transform the strings coming from the dataset into their corresponding type (e.g. integer).
- If the same book was a bestseller in two different years then it will appear twice in the csv. We want both entries to go to the same object to avoid duplicates, but add both years to the object. 
- Consider using a dictionary with the titles as keys and objects as values. This way you can access the object again and add another year. The result `bestsellers` will still be a list of Books.

### Task 4: Find the Year with the Most Popular and Enjoyable Books (15%)

Create the `best_year_rating()` method in the `Amazon` class.
The method has no parameters and returns an integer that represents the year with the best median rating. Consider using the `statistics` module to calculate the median value for each year.

Create the `best_year_reviews()` method in the `Amazon` class.
The method has no parameters and returns an integer that represents the year with the best median reviews. Consider using the `statistics` module to calculate the median value for each year.

### Task 5: Recommend Books (20%)

- Add the attribute `recommended` (Boolean) to the `Book` class and set it to `False`. Do not modify the list of parameters of the constructor.
- Create the method `recommend()` in the `Book` class. The method receives a rating and a number of reviews, and it does not return anything. If the fiction book has a rating that is at least that of the first parameter and a number of reviews at least that of the second parameter, its `recommended` attribute must be set to `True`.
- Create the methods `recommend_book()`  in the `Amazon` class. The method receives a rating and a number of reviews. The method does not return anything. Instead, it iterates over the list of books and calls the  corresponding `recommend()` method to recommend all books that fulfill the given requirements.
- Finally, create the method `get_recommendations()` in the `Amazon` class. The method has no parameters and returns a list of strings with the string representation (i.e. `str()`) of all recommended books (both fiction and non-fiction books).


