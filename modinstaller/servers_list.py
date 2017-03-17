import wx
import modinstaller.main_window

sizer = wx.BoxSizer(wx.VERTICAL)

listbox = wx.ListBox(modinstaller.main_window.window,choices=["unchi","site?"])

sizer.Add(listbox, 1, wx.ALL | wx.EXPAND)

modinstaller.main_window.add(listbox)

def enabled():
    return