import wx
import wx.lib.intctrl
import math

#функция обработки события кнопки
def onButtonClick(frame):
    a = getA.GetValue()
    b = getB.GetValue()
    c = getC.GetValue()
    d = getD.GetValue()
    e = getE.GetValue()
    f = getF.GetValue()
    if a == 0:
        y = e / b
        x = (f - d * y) / c
        result = "X:= %s \nY:= %s" % (x, y)
    else:
        y = (a * f - e * c) / (a * d - b * c)
        x = (e - b * y) / a
        result = "X:= %s \nY:= %s" % (x, y)
        text5.SetLabel(result)

app = wx.App()
frame = wx.Frame(None, title = 'Система линейных уравнений',size=(600, 250), style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
mainPanel = wx.Panel(frame)

#создаем главный бокссайзер, в нем располагаем четыре горизонтальных бокссайзера
vboxMain = wx.BoxSizer(wx.VERTICAL)
vboxFirstLine = wx.BoxSizer()
vboxDopLine = wx.BoxSizer()
vboxSecondLine = wx.BoxSizer()
vboxThridLine = wx.BoxSizer()

#создаем элементы, которые будут находиться в бокссайзерах
text1 = wx.StaticText(mainPanel, label="x      + ")
text2 = wx.StaticText(mainPanel, label="y      = ")
text3 = wx.StaticText(mainPanel, label="x      + ")
text6 = wx.StaticText(mainPanel, label="y      = ")
button = wx.Button(mainPanel, wx.ID_ANY, label="Решить", size=(100, 50))
text4 = wx.StaticText(mainPanel, label= "Решение:")
text5 = wx.StaticText(mainPanel, label= "")

getA = wx.lib.intctrl.IntCtrl(mainPanel)
getA.SetMinSize(size = (40, 20))
getB = wx.lib.intctrl.IntCtrl(mainPanel)
getB.SetMinSize(size = (40, 20))
getC = wx.lib.intctrl.IntCtrl(mainPanel)
getC.SetMinSize(size = (40, 20))
getD = wx.lib.intctrl.IntCtrl(mainPanel)
getD.SetMinSize(size = (40, 20))
getE = wx.lib.intctrl.IntCtrl(mainPanel)
getE.SetMinSize(size = (40, 20))
getF = wx.lib.intctrl.IntCtrl(mainPanel)
getF.SetMinSize(size = (40, 20))

#первый бокссайзер
vboxFirstLine.Add(getA, flag = wx.ALL, border = 7)
vboxFirstLine.Add(text1, flag = wx.ALL, border = 10)
vboxFirstLine.Add(getB, flag = wx.ALL, border = 7)
vboxFirstLine.Add(text2, flag = wx.ALL, border = 10)
vboxFirstLine.Add(getC, flag = wx.ALL, border = 7)

vboxMain.Add(vboxFirstLine, wx.EXPAND)

#доп бокссайзер
vboxDopLine.Add(getD, flag = wx.ALL, border = 7)
vboxDopLine.Add(text3, flag = wx.ALL, border = 10)
vboxDopLine.Add(getE, flag = wx.ALL, border = 7)
vboxDopLine.Add(text6, flag = wx.ALL, border = 10)
vboxDopLine.Add(getF, flag = wx.ALL, border = 7)

vboxMain.Add(vboxDopLine, wx.EXPAND)

#второй бокссайзер
vboxSecondLine.Add(button)
frame.Bind(wx.EVT_BUTTON, onButtonClick)
vboxMain.Add(vboxSecondLine, flag = wx.ALIGN_CENTER)

#третий бокссайзер
vboxThridLine.Add(text4, flag = wx.ALL, border =20)
vboxThridLine.Add(text5, flag = wx.ALL, border =20)
vboxMain.Add(vboxThridLine, flag = wx.ALIGN_LEFT)

mainPanel.SetSizer(vboxMain)
frame.Show()
app.MainLoop()
