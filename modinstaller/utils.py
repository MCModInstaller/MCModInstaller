import wx
def bind(control, bind_type):
    def bind_(func):
        control.Bind(bind_type, func)
    return bind_
def clicked(control):
    def closed_(func):
        control.Bind(wx.EVT_BUTTON, func)
    return bind_