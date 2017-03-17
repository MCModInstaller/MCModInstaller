import wx
app = wx.App()

import modinstaller.main_window


import modinstaller.servers_list
modinstaller.servers_list.enabled()

modinstaller.main_window.window.Fit()
modinstaller.main_window.show()

app.MainLoop()