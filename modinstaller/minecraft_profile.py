import sys
import os
import wx
import modinstaller.main_window
import json
from modinstaller.utils import bind
HOME = os.environ.get("HOME","")
MINECRAFT_DIR = None
class ErrorDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, modinstaller.main_window.window)
        self.Title = "エラー - MCModInstaller"
        self.no_exit = False
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="Minecraftのランチャーの設定が見つかりません。\nランチャーを一度も起動していない場合は、ランチャーを起動してください。\nbatファイルなどで.minecraftディレクトリの場所を変更している場合は、.minecraftディレクトリを指定してください。")
        self.sizer.Add(label,0,wx.ALL, 10)
        set_dir_button = wx.Button(self, label="場所を指定")
        set_dir_button.Bind(wx.EVT_BUTTON, self.set_dir_button_clicked)
        research_button = wx.Button(self, label="再検索")
        research_button.Bind(wx.EVT_BUTTON, self.research_button_clicked)
        exit_button = wx.Button(self, label="終了")
        exit_button.Bind(wx.EVT_BUTTON, self.exit_button_clicked)
        self.buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons_sizer.Add((1,1),1)
        self.buttons_sizer.Add(set_dir_button, 0, wx.RIGHT, 5)
        self.buttons_sizer.Add(research_button, 0, wx.RIGHT, 5)
        self.buttons_sizer.Add(exit_button, 0, wx.RIGHT, 5)
        self.buttons_sizer.Add((10,0))
        self.sizer.Add(self.buttons_sizer,0,wx.EXPAND | wx.BOTTOM | wx.LEFT | wx.RIGHT ,10)
        self.SetSizer(self.sizer)
        self.Fit()
        self.Bind(wx.EVT_CLOSE, self.closed)
    def set_dir_button_clicked(self, e):
        dialog = wx.DirDialog(self)
        dialog.SetMessage(".minecraftディレクトリを選択 - MCModInstaller")
        if dialog.ShowModal() == wx.ID_OK:
            self.no_exit = True
            self.Close()
            search_minecraft_profile()
    def research_button_clicked(self, e):
        self.no_exit = True
        self.Close()
        search_minecraft_profile()
    def exit_button_clicked(self, e):
        sys.exit(0)
    def closed(self, e):
        if not self.no_exit:
            sys.exit(0)
        else:
            self.no_exit = False
            self.Destroy()

def minecraft_profile_check(dir):
    print("searching "+dir)
    ret = os.path.exists(dir+os.sep+"launcher_profiles.json")
    if ret:
        global MINECRAFT_DIR
        MINECRAFT_DIR = dir
    return ret
def search_minecraft_profile():
    minecraft_profile_check(HOME+("/Library/Application Support/minecraft".replace("/",os.sep))) # macOS
    minecraft_profile_check(os.environ.get("APPDATA",HOME+os.sep+"AppData"+os.sep+"Roaming")+("/.minecraft".replace("/",os.sep))) # Windows Vista~
    # minecraft_profile_check(HOME+("/Application Data/.minecraft".replace("/",os.sep))) # Windows XP
    minecraft_profile_check(HOME+("/.minecraft".replace("/",os.sep))) # Linux
    if MINECRAFT_DIR: # Minecraftのフォルダがある
        return
    dialog = ErrorDialog()
    dialog.ShowModal()
def get_profiles():
    return json.load(open(MINECRAFT_DIR+os.sep+"launcher_profiles.json")).get("profiles",{})
search_minecraft_profile()
print(get_profiles())
