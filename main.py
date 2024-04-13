import gdown
import wx


def initFrame():
    app = wx.App()
    frame = wx.Frame(parent=None, title='Header 001')
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    initFrame()