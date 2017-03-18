import sys
import os
import wx
import modinstaller.main_window
from modinstaller.utils import bind
HOME = os.environ.get("HOME","")
MINECRAFT_DIR = None
def minecraft_profile_check(dir):
    print("searching "+dir)
    ret = os.path.exists(dir+os.sep+"launcher_profiles.json")
    if ret:
        global MINECRAFT_DIR
        MINECRAFT_DIR = dir
    return ret

def search_minecraft_profile():
    minecraft_profile_check(HOME+("/Library/Application Support/minecraft".replace("/",os.sep)))
    minecraft_profile_check(HOME+("/AppData/Roaming/.minecraft".replace("/",os.sep)))
    # minecraft_profile_check(HOME+("/Application Data/.minecraft".replace("/",os.sep))) # Windows XP
    minecraft_profile_check(HOME+("/.minecraft".replace("/",os.sep)))
    dialog = wx.Dialog(modinstaller.main_window.window)
    dialog.SetTitle("エラー - MCModInstaller")
    dialog_sizer = wx.BoxSizer(wx.VERTICAL)
    label = wx.StaticText(dialog, label="Minecraftのランチャーの設定が見つかりません。\nランチャーを一度も起動していない場合は、ランチャーを起動してください。\nbatファイルなどで.minecraftディレクトリの場所を変更している場合は、.minecraftディレクトリを指定してください。")
    dialog_sizer.Add(label,0,wx.ALL, 10)
    set_dir_button = wx.Button(dialog, label="場所を指定")
    @bind(set_dir_button, wx.EVT_BUTTON)
    def set_dir_button_clicked(e):
        print("push set dir")
    research_button = wx.Button(dialog, label="再検索")
    @bind(research_button, wx.EVT_BUTTON)
    def research_button_clicked(e):
        dialog.Close()
        search_minecraft_profile()
    exit_button = wx.Button(dialog, label="終了")
    @bind(exit_button, wx.EVT_BUTTON)
    def exit_button_clicked(e):
        sys.exit(0)
    dialog_buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
    dialog_buttons_sizer.Add((1,1),1)
    dialog_buttons_sizer.Add(set_dir_button, 0, wx.RIGHT, 5)
    dialog_buttons_sizer.Add(research_button, 0, wx.RIGHT, 5)
    dialog_buttons_sizer.Add(exit_button, 0, wx.RIGHT, 5)
    dialog_buttons_sizer.Add((10,0))
    dialog_sizer.Add(dialog_buttons_sizer,0,wx.EXPAND | wx.BOTTOM | wx.LEFT | wx.RIGHT ,10)
    dialog.SetSizer(dialog_sizer)
    dialog.Fit()
    dialog.ShowModal()
search_minecraft_profile()