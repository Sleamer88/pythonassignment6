"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

import wx
import wx.lib.scrolledpanel as scrolled
import books.books_types as books_types
import books.books_utils as books_utils


class GUI(wx.Frame):
    """
    Represents the GUI of the program.
    """

    def __init__(self) -> None:
        super().__init__(parent=None, title='Bestseller Books', size=wx.Size(560, 700))
        self.upload_data()

        self.top_panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # First panel
        self.panel1 = wx.Panel(self.top_panel)
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)

        header_path = books_utils.get_absolute_path('assets/goodreads.png')
        header = wx.Bitmap(header_path)
        img_header = wx.StaticBitmap(self.panel1, -1, header, wx.DefaultPosition)
        self.sizer1.Add(img_header, 0, wx.CENTER | wx.EXPAND, 5)

        subtitle_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        subtitle1 = wx.StaticText(self.panel1, -1, 'Recommend Bestsellers')
        subtitle1.SetFont(subtitle_font)
        self.sizer1.Add(subtitle1, 0, wx.ALL | wx.EXPAND, 5)

        intro_msg = 'Recommend Amazon bestsellers that meet your requirments. See below.'
        lbl_intro = wx.StaticText(self.panel1, -1, intro_msg)
        self.sizer1.Add(lbl_intro, 0, wx.ALL | wx.EXPAND, 5)

        line = wx.StaticLine(self.panel1)
        self.sizer1.Add(line, 0, wx.ALL | wx.EXPAND, 5)

        subtitle2 = wx.StaticText(self.panel1, -1, 'Recommendation Criterias')
        subtitle2.SetFont(subtitle_font)
        self.sizer1.Add(subtitle2, 0, wx.ALL | wx.EXPAND, 5)

        recommend_rating = 'Enter the minimum rating.'
        self.lbl_recommend_rating = wx.StaticText(self.panel1, -1, recommend_rating)
        self.sizer1.Add(self.lbl_recommend_rating, 0, wx.ALL | wx.EXPAND, 5)

        self.txt_rating = wx.TextCtrl(self.panel1)
        self.sizer1.Add(self.txt_rating, 0, wx.ALL | wx.EXPAND, 5)

        recommend_reviews = 'Enter the minimum reviews.'
        self.lbl_recommend_reviews = wx.StaticText(self.panel1, -1, recommend_reviews)
        self.sizer1.Add(self.lbl_recommend_reviews, 0, wx.ALL | wx.EXPAND, 5)

        self.txt_reviews = wx.TextCtrl(self.panel1)
        self.sizer1.Add(self.txt_reviews, 0, wx.ALL | wx.EXPAND, 5)

        self.lbl_recommend_error = wx.StaticText(self.panel1, -1, '')
        self.sizer1.Add(self.lbl_recommend_error, 0, wx.ALL | wx.EXPAND, 5)

        self.btn_recommend = wx.Button(self.panel1, label='Find')
        self.btn_recommend.Bind(wx.EVT_BUTTON, self.print_recommendation_panel)
        self.sizer1.Add(self.btn_recommend, 0, wx.ALL | wx.CENTER, 5)

        line = wx.StaticLine(self.panel1)
        self.sizer1.Add(line, 0, wx.ALL | wx.EXPAND, 5)

        subtitle3 = wx.StaticText(self.panel1, -1, 'Results')
        subtitle3.SetFont(subtitle_font)
        self.sizer1.Add(subtitle3, 0, wx.ALL | wx.EXPAND, 5)

        self.panel1.SetSizer(self.sizer1)
        self.sizer.Add(self.panel1, 0, wx.ALL | wx.EXPAND, 5)

        self.top_panel.SetSizer(self.sizer)
        self.Show()

    def upload_data(self) -> None:
        """
        Creates an instance of the Netflix system.
        """

        path = books_utils.get_absolute_path('data/books.csv')
        self.books = books_types.Amazon([])
        self.books.read_books_csv(path)

        # Instantiate the recommended books list
        self.recommendations = []

    def print_recommendation_panel(self, event) -> None:
        """
        Prints a new panel with all recommended books.
        :param event: click event
        """

        try:
            errors = [0,0,0]
            error_text = ['Automatic rating: 0', 'Automatic reviews: 0', 'Automatic genre: Both']
            if self.txt_rating.GetValue() is '':
                rating = 0
                errors[0] = 1
            else:
                rating = float(self.txt_rating.GetValue())

            if self.txt_reviews.GetValue() is '':
                reviews = 0
                errors[1] = 1
            else:
                reviews = int(self.txt_reviews.GetValue())

            self.books.recommend_book(rating, reviews)
            self.recommendations = self.books.get_recommendations()

            text = ''
            for error in range(len(errors)):
                if errors[error] == 1:
                    text += error_text[error] + '\n'
            self.lbl_recommend_error.SetLabel(text)

        except Exception as e:
            self.lbl_recommend_error.SetLabel('Please, introduce valid integer values.')


        if hasattr(self, 'panel2'):
            self.panel2.Destroy()

        # Create new panel
        self.panel2 = scrolled.ScrolledPanel(self.top_panel, -1, size=wx.Size(530, 300))
        self.panel2.SetupScrolling()
        self.panel2.SetBackgroundColour('#FFF')

        self.sizer2 = wx.BoxSizer(wx.VERTICAL)

        for r in self.recommendations:
            lbl = wx.StaticText(self.panel2, -1, r)
            self.sizer2.Add(lbl, 0, wx.ALL | wx.EXPAND, 5)

        self.panel2.SetSizer(self.sizer2)

        self.sizer.Add(self.panel2, 0, wx.ALL | wx.EXPAND, 5)
        self.top_panel.SetSizer(self.sizer)
        self.sizer.Layout()
        self.Layout()
