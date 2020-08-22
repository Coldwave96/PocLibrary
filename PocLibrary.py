# -*- coding: utf-8 -*-
import wx
import gui


if __name__ == '__main__':
    app = wx.App()

    main_win = gui.MyFrame1(parent=None)
    main_win.Show()

    app.MainLoop()