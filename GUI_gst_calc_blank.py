import wx
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='gst calculator')
        panel = wx.Panel(self)        
        sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        btn_1 = wx.Button(panel, label='Press Me')
        btn_1.Bind(wx.EVT_BUTTON, self.on_press)
        sizer.Add(btn_1, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(sizer)        
        self.Show()
    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
