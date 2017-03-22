import wx
import modinstaller.minecraft_profile
import modinstaller.main_window
import modinstaller.tabs.meta

notebook = wx.Notebook(modinstaller.main_window.window)
notebook.AddPage(modinstaller.tabs.meta.MetaPage(notebook), "情報")
modinstaller.main_window.add(notebook)