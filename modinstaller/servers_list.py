import wx
import modinstaller.minecraft_profile
import modinstaller.main_window

sizer = wx.BoxSizer(wx.VERTICAL)

listbox = wx.ListBox(modinstaller.main_window.window,choices=["ここにサーバー一覧"])

sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

add_button = wx.Button(modinstaller.main_window.window,label="Add MOD Profile")

sizer_2.Add(add_button)

sizer.Add(listbox, 1, wx.ALL | wx.EXPAND)
sizer.Add(sizer_2, 0, wx.TOP | wx.EXPAND, 10)

modinstaller.main_window.add(sizer)

def enabled():
    return