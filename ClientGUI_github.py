#Implementation of chat client using wxpython and socket library.
#Implemented by Aditya Kaushik(www.github.com/FuriousFlash) and Puja Kumari(www.github.com/PujaLuciX)
#Further additions and improvements in progress.

import wx
import wx.richtext as rt
import sys
import socket
import thread

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name
host = "192.168.1.100"                           
port = 9999
# connection to hostname on the port.
s.connect((host, port))

class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title):
        super(MainWindow, self).__init__(parent, ID, title=title,size=(450,400))
        panel=wx.Panel(self)
        vbox=wx.BoxSizer(wx.VERTICAL)

        hbox=wx.BoxSizer(wx.HORIZONTAL)
        font=wx.Font(12, wx.MODERN, wx.ITALIC, wx.BOLD, underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        self.usertext = rt.RichTextCtrl(panel, style=wx.TE_MULTILINE | wx.BORDER_SUNKEN | wx.TE_READONLY | wx.TE_RICH2)
        #self.usertext.SetFont(font)
        hbox.Add(self.usertext ,proportion=1 , flag=wx.EXPAND)
        vbox.Add(hbox, proportion=3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        vbox.Add((-1,10))

        h1box=wx.BoxSizer(wx.HORIZONTAL)
        m=wx.StaticText(panel,label= "Write a          \nmessage ...    ")
        h1box.Add(m, flag=wx.EXPAND|wx.CENTER, border=5)
        self.t=wx.TextCtrl(panel, -1, " ",style = wx.TE_MULTILINE)
        h1box.Add(self.t, proportion=1, flag=wx.EXPAND)
        vbox.Add(h1box, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add((-1,10))

        Press = wx.Button(panel, label= "Submit")
        Press.Bind(wx.EVT_BUTTON, self.inserttext)
        h2box=wx.BoxSizer(wx.HORIZONTAL)
        h2box.Add(Press, proportion=1)
        vbox.Add(h2box, proportion=0, flag=wx.ALIGN_CENTER, border=10)
        vbox.Add((-1,25))

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def inserttext(self, event):
        p=self.t.GetValue()
        self.usertext.WriteText("\n")
        self.usertext.BeginBold()
        self.usertext.BeginUnderline()
        self.usertext.WriteText("CLIENT :")
        self.usertext.EndBold()
        self.usertext.EndUnderline()
        self.usertext.WriteText("  ")
        self.usertext.WriteText(p)
        s.sendall(p.encode('ascii'))
        self.t.Clear()

class MainApp(wx.App):
    def OnInit(self):
        self.myWindow = MainWindow(None, -1, "Chatting App")
        self.myWindow.Show(True)
        self.SetTopWindow(self.myWindow)
        return(True)

AppStart = MainApp(0)

def Receive():
    while True:
        p=s.recv(1024)
        AppStart.myWindow.usertext.WriteText("\n")
        AppStart.myWindow.usertext.BeginBold()
        AppStart.myWindow.usertext.BeginUnderline()
        AppStart.myWindow.usertext.WriteText("SERVER :")
        AppStart.myWindow.usertext.EndBold()
        AppStart.myWindow.usertext.EndUnderline()
        AppStart.myWindow.usertext.WriteText("  ")
        AppStart.myWindow.usertext.WriteText(p.decode('ascii'))
    #s.close()
    
thread.start_new_thread(Receive,())
AppStart.MainLoop()

