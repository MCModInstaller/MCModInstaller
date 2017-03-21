import wx
import modinstaller.minecraft_profile

class ServersListSizer(wx.BoxSizer):
    def __init__(self, parent):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        self.listbox = wx.ListBox(parent,choices=["ここにサーバー一覧"])
        self.sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.add_button = wx.Button(parent,label="Add MOD Profile")
        self.sizer_2.Add(self.add_button)
        self.Add(self.listbox, 1, wx.ALL | wx.EXPAND)
        self.Add(self.sizer_2, 0, wx.TOP | wx.EXPAND, 10)

def enabled():
    return