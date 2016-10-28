#Implementation of chat server using wxpython and socket library.
#Implemented by Aditya Kaushik(www.github.com/FuriousFlash) and Puja Kumari(www.github.com/PujaLuciX)

import wx
import socket
import time
import thread
import wx.richtext as rt

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = '192.168.1.100'
port = 9999                                         

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)
clientsocket=''

class Example(wx.Frame):
    global clientsocket
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(390, 350))
            
        self.InitUI()
        self.Centre()
        self.Show()     

    def InitUI(self):
    
        panel = wx.Panel(self)
        font = wx.Font(18, wx.MODERN, wx.ITALIC, wx.NORMAL, underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Chat ROM')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc2 = rt.RichTextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_RICH | wx.TE_READONLY)
        font2 = wx.Font(10, wx.MODERN, wx.ITALIC, wx.NORMAL)
        self.tc2.SetFont(font2)
        hbox3.Add(self.tc2, proportion=1, flag=wx.EXPAND)
        self.tc2.GetCaret().Hide() 
        vbox.Add(hbox3, proportion=3, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

        vbox.Add((-1, 10))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Message')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_RICH)
        hbox1.Add(self.tc, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox1, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT , border=10)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn1.Bind(wx.EVT_BUTTON,self.insert)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)

    def insert(self,e):
        self.tc2.BeginBold()
        r.tc2.BeginTextColour((0,255,0))
        self.tc2.WriteText("Server:")
        r.tc2.EndTextColour()
        self.tc2.EndBold()
        l=self.tc.GetValue()
        self.tc2.WriteText(l)
        self.tc2.Newline()
        clientsocket.sendall(l)
        self.tc.Clear()


if __name__ == '__main__':
  
    app = wx.App()
    r=Example(None, title='Chat App')
        

    # queue up to 5 requests
    def GetConnected():
        serversocket.listen(5)                                           
        global clientsocket
        # establish a connection
        clientsocket,addr = serversocket.accept()
        font3 = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL, underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        u="Got a connection from "+ str(addr)+"\n"
        r.tc2.WriteText(u)
        r.tc2.BeginAlignment(rt.TEXT_ALIGNMENT_RIGHT)
        r.tc2.BeginLineSpacing(rt.TEXT_ATTR_LINE_SPACING_HALF)
        r.tc2.EndLineSpacing()
        r.tc2.EndAlignment()
        
    
        while True:
            try:
                d=clientsocket.recv(1024)
                r.tc2.BeginBold()
                r.tc2.BeginTextColour((255,0,0))
                r.tc2.WriteText("Client:")
                r.tc2.EndTextColour()
                r.tc2.EndBold()
                r.tc2.WriteText(d.decode('ascii'))
                r.tc2.Newline()
            except:
                r.tc2.WriteText("DCED\n")
                GetConnected()
        clientsocket.close()

    thread.start_new_thread(GetConnected,())
    app.MainLoop()
