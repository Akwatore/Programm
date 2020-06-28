import wx
import wx.lib.intctrl
import math

#функция обработки события кнопки 
def onButtonClick(frame):
    a = getA.GetValue()
    b = getB.GetValue()
    c = getC.GetValue()
    D = b * b - 4 * a * c
    if D > 0:
        X1 = (-b + math.sqrt(D)) / 2 * a
        X2 = (-b - math.sqrt(D)) / 2 * a
        result = "X1:= %s \nX2:= %s" % (X1, X2)
    else:
        result = "Дискриминант меньше 0"
    text5.SetLabel(result)

app = wx.App()
frame = wx.Frame(None, title = 'Кв. уравнение',size=(300, 200), style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
mainPanel = wx.Panel(frame)

#создаем главный бокссайзер, в нем располагаем три горизонтальных бокссайзера
vboxMain = wx.BoxSizer(wx.VERTICAL)
vboxFirstLine = wx.BoxSizer()
vboxSecondLine = wx.BoxSizer()
vboxThridLine = wx.BoxSizer()

#создаем элементы, которые будут находиться в бокссайзерах
text1 = wx.StaticText(mainPanel, label="A =")
text2 = wx.StaticText(mainPanel, label="B =")
text3 = wx.StaticText(mainPanel, label="C =")
button = wx.Button(mainPanel, wx.ID_ANY, label="Решить", size=(100, 50))
text4 = wx.StaticText(mainPanel, label= "Решение:")
text5 = wx.StaticText(mainPanel, label= "")

getA = wx.lib.intctrl.IntCtrl(mainPanel)
getA.SetMinSize(size = (40, 20))
getB = wx.lib.intctrl.IntCtrl(mainPanel)
getB.SetMinSize(size = (40, 20))
getC = wx.lib.intctrl.IntCtrl(mainPanel)
getC.SetMinSize(size = (40, 20))

#первый бокссайзер
vboxFirstLine.Add(text1, flag = wx.ALL, border = 10)
vboxFirstLine.Add(getA, flag = wx.ALL, border = 7)
vboxFirstLine.Add(text2, flag = wx.ALL, border = 10)
vboxFirstLine.Add(getB, flag = wx.ALL, border = 7)
vboxFirstLine.Add(text3, flag = wx.ALL, border = 10)
vboxFirstLine.Add(getC, flag = wx.ALL, border = 7)
vboxMain.Add(vboxFirstLine, wx.EXPAND)

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
