import wx
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='gst calculator')
        panel = wx.Panel(self)        
        #sizer = wx.BoxSizer(wx.VERTICAL)        
        #self.text_ctrl = wx.TextCtrl(panel)
        #sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        
        box1 =wx.StaticBox(panel,label='Add Items',pos=(5,5),size=(240,600))
        box2= wx.StaticBox(panel,label='Items in Cart',pos=(245,5),size=(480,600))
        db_label1= wx.StaticText(panel,label='Product name:',pos=(7,30))
        db_label2= wx.StaticText(panel,label='Price per Unit:',pos=(7,90))
        db_label3= wx.StaticText(panel,label='Product Type:',pos=(7,150))
        db_label4= wx.StaticText(panel,label='GST:',pos=(7,220))
        
        #btn_1 = wx.Button(panel, label='Add item',pos=(1200,600))
        #btn_1.Bind(wx.EVT_BUTTON, self.on_press)
        cb_product_name=wx.ComboBox(panel,pos=(10,50),style=wx.CB_DROPDOWN)
        cb_product_cost=wx.ComboBox(panel,pos=(10,110),style=wx.CB_DROPDOWN)
        cb_product_type=wx.ComboBox(panel,pos=(10,170),style=wx.CB_DROPDOWN)
        

        
        #sizer.Add(btn_1, 0, wx.ALL)        
        #panel.SetSizer(sizer)        
        self.Show()
    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("Nothing to add!")
        else:
            print(f'You typed: "{value}"')
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
