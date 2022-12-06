"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""


from books.gui import GUI
import wx

if __name__ == '__main__':
    app = wx.App()
    gui = GUI()
    app.MainLoop()