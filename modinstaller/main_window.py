import wx

window = wx.Frame(None)

window.Title = "MCModInstaller"

sizer = wx.BoxSizer(wx.HORIZONTAL)


def add(sizer_):
    sizer.Add(sizer_, 1, wx.ALL | wx.EXPAND, 10)

def show():
    window.SetSizer(sizer)
    window.Show()