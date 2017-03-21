import wx
app = wx.App()

import modinstaller.main_window


import modinstaller.servers_list
import modinstaller.main_tab
modinstaller.main_window.window.Show()

app.MainLoop()
