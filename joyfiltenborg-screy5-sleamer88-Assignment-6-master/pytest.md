# PyTest

This tutorial will give a brief overview of how to test your application using PyTest.

**Note:** Through this tutorial there will be multiple commandline input examples like:
```
python -m pip install pytest
```
It could be that the first argument `python` is different for your installation or operating system. the main examples are `py` for windows and `pythonw` on Mac. The rest of the tutorial will just use `python` so please replace this with the approprriate notation for your system.

## Installation
The easiest way to install PyTest is described in python-interpreter-wxpython.pdf although this is PyCharm only.

Using `pip` it is also fairly straightforward to install PyTest, using one of the following commands:
```
pip install pytest
#or
python -m pip install pytest
#or for those of you with anaconda
conda install -c anaconda pytest
```

## Usage
PyTest will automatically search for files pre-faced with `test_`. So you need to simply run it in the terminal from the correct location. Open your assignment-6 folder in the terminal either in PyCharm with `view>tool windows> Terminal` or in VScode with `terminal> New terminal`. Run one of these commands:
```
pytest
#or
python -m pytest
```

## Results
If everything works correctly PyTest will run all available tests and output information on those that your code has failed. Look at the example output below. after FAILED the location of the test file is given followed by :: and the particular test function that failed. Finally there is the type of error and some message describing what went wrong. We have included the task that the test belongs to insiide this message. 

```
======================================= short test summary info ======================================= 
FAILED tests/test_books_types.py::test_amazon_attrs - AssertionError: [Task 1] The Amazon object do not have the bestsellers attribute
FAILED tests/test_books_types.py::test_fiction_str - AssertionError: [Task 2] The FictionBook __str__() method is incorrect. Expected: Catching Fire (The Hunger Games): Fiction (2010) - Obtained: Catching Fire (Th...
FAILED tests/test_books_types.py::test_nonfiction_str - AssertionError: [Task 2] The NonFictionBook __str__() method is incorrect. Expected: Calm the F*ck Down: An Irreverent Adult Coloring Book (Irreverent Book Seri...
FAILED tests/test_books_types.py::test_list_of_bestsellers_length - AttributeError: 'Amazon' object has no attribute 'bestsellers'
FAILED tests/test_books_types.py::test_fiction_length - AttributeError: 'Amazon' object has no attribute 'bestsellers'
FAILED tests/test_books_types.py::test_nonfiction_length - AttributeError: 'Amazon' object has no attribute 'bestsellers'
FAILED tests/test_books_types.py::test_list_of_bestsellers_content - AttributeError: 'Amazon' object has no attribute 'bestsellers'
FAILED tests/test_books_types.py::test_replace_empty_str - AttributeError: 'Amazon' object has no attribute 'bestsellers'
FAILED tests/test_books_types.py::test_find_best_rating - AssertionError: [Task 4] The year with best ratings is incorrect. Expected: 2019 - Obtained: 2012
FAILED tests/test_books_types.py::test_find_best_reviews - AssertionError: [Task 4] The year with best reviews is incorrect. Expected: 2019 - Obtained: 2012
FAILED tests/test_books_types.py::test_recommend_fiction_rating - AssertionError: [Task 5] The FictionBook has been recommended when it does not have the required rating.
FAILED tests/test_books_types.py::test_recommend_fiction_reviews - AssertionError: [Task 5] The FictionBook has been recommended when it does not have the required reviews.
FAILED tests/test_books_types.py::test_recommend_nonfiction_rating - AssertionError: [Task 5] The NonFictionBook has been recommended when it does not have the required rating.
FAILED tests/test_books_types.py::test_recommend_nonfiction_reviews - AssertionError: [Task 5] The NonFictionBook has been recommended when it does not have the required reviews.
==================================== 14 failed, 19 passed in 0.88s ====================================
```

If you scroll up you can see more details about the individual tests containing the test code and the line where the error occurred.

```
_________________________________test_amazon_attrs __________________________________

    def test_amazon_attrs():
        amazon = Amazon([])
        result = hasattr(amazon, 'bestsellers')

        msg = '[Task 1] The Amazon object do not have the bestsellers attribute'
>       assert result, msg
E       AssertionError: [Task 1] The Amazon object do not have the bestsellers attribute
E       assert False

tests\test_books_types.py:123: AssertionError
```

Finally once you have completed all tasks your output should be:
**Note** that all passing unit tests does not mean that your assignment is perfect. However, failing tests means that your assignment contains errors, such as incomplete tasks or bad code.
```
========================================= test session starts ==========================================
platform information
rootdir:   Path\to\assignment
collected 33 items

tests\test_books_types.py .................................                                                                                                   [100%]

========================================== 33 passed in 0.31s ========================================== 
```