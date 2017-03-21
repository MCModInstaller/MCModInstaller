import wx
import modinstaller.servers_list

class MainWindow(wx.Frame):
    def __init__(self, parent = None):
        wx.Frame.__init__(self,parent)
        self.Title = "MCModInstaller"
        self.Sizer = wx.BoxSizer(wx.HORIZONTAL)
    def Add(self, sizer):
        self.Sizer.Add(sizer, 1, wx.ALL | wx.EXPAND, 10)

window = MainWindow()
window.Add(modinstaller.servers_list.ServersListSizer(window))
add = window.Add