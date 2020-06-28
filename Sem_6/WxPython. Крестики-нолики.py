import random
import wx
import wx.lib.buttons as buttons

class KRPanel(wx.Panel):
    #Панель объектов

    def __init__(self, parent):
        """
        Инициализация панели
        """
        wx.Panel.__init__(self, parent)
        self.toggled = False
        self.playerWon = False

        self.layoutWidgets()

    def checkWin(self, computer=False):
        """
        Проверки на выигрыш
        """
        for button1, button2, button3 in self.methodsToWin:
            if button1.GetLabel() == button2.GetLabel() and \
               button2.GetLabel() == button3.GetLabel() and \
               button1.GetLabel() != "":
                print("Игрок выиграл!")
                self.playerWon = True
                button1.SetBackgroundColour("Yellow")
                button2.SetBackgroundColour("Yellow")
                button3.SetBackgroundColour("Yellow")
                self.Layout()

                if not computer:
                    msg = "Ты выиграл! Хочешь сыграть ещё раз?"
                    dlg = wx.MessageDialog(None, msg, "Победитель!",
                                           wx.YES_NO | wx.ICON_WARNING)
                    result = dlg.ShowModal()
                    if result == wx.ID_YES:
                        wx.CallAfter(self.restart)
                    dlg.Destroy()
                    break
                else:
                    return True

    def layoutWidgets(self):
        """
        Создание и настройка кнопок и виджетов
        """
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.fgSizer = wx.FlexGridSizer(rows=3, cols=3, vgap=5, hgap=5)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        size = (100,100)
        self.button1 = buttons.GenToggleButton(self, size=size, name="btn1")
        self.button2 = buttons.GenToggleButton(self, size=size, name="btn2")
        self.button3 = buttons.GenToggleButton(self, size=size, name="btn3")
        self.button4 = buttons.GenToggleButton(self, size=size, name="btn4")
        self.button5 = buttons.GenToggleButton(self, size=size, name="btn5")
        self.button6 = buttons.GenToggleButton(self, size=size, name="btn6")
        self.button7 = buttons.GenToggleButton(self, size=size, name="btn7")
        self.button8 = buttons.GenToggleButton(self, size=size, name="btn8")
        self.button9 = buttons.GenToggleButton(self, size=size, name="btn9")
        self.normalBtnColour = self.button1.GetBackgroundColour()

        self.widgets = [self.button1, self.button2, self.button3,
                        self.button4, self.button5, self.button6,
                        self.button7, self.button8, self.button9]

        # изменение шрифта кнопок и привязка к событию
        for button in self.widgets:
            button.SetFont(font)
            button.Bind(wx.EVT_BUTTON, self.onToggle)

        # добавление виджета на сайзер
        self.fgSizer.AddMany(self.widgets)
        mainSizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)

        self.endTurnBtn = wx.Button(self, label="Завершить ход")
        self.endTurnBtn.Bind(wx.EVT_BUTTON, self.onEndTurn)
        self.endTurnBtn.Disable()
        btnSizer.Add(self.endTurnBtn, 0, wx.ALL|wx.CENTER, 5)

        startOverBtn = wx.Button(self, label="Перезапуск игры")
        startOverBtn.Bind(wx.EVT_BUTTON, self.onRestart)
        btnSizer.Add(startOverBtn, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER)

        self.methodsToWin = [(self.button1, self.button2, self.button3),
                             (self.button4, self.button5, self.button6),
                             (self.button7, self.button8, self.button9),
                             # победа по горизонтали
                             (self.button1, self.button4, self.button7),
                             (self.button2, self.button5, self.button8),
                             (self.button3, self.button6, self.button9),
                             # победа по вертикали
                             (self.button1, self.button5, self.button9),
                             (self.button3, self.button5, self.button7)]
                             # победа по диагонали
        self.SetSizer(mainSizer)

    def enableUnusedButtons(self):
        """
        Включает неиспользованные кнопки
        """
        for button in self.widgets:
            if button.GetLabel() == "":
                button.Enable()
        self.Refresh()
        self.Layout()

    def onEndTurn(self, event):
        """
        Игра компьютера
        """
        self.toggled = False

        # Отключить все воспроизводимые кнопки
        for btn in self.widgets:
            if btn.GetLabel():
                btn.Disable()

        computerPlays = []
        noPlays = []

        for button1, button2, button3 in self.methodsToWin:
            if button1.GetLabel() == button2.GetLabel() and button3.GetLabel() == "":
                if button1.GetLabel() == "" and button2.GetLabel() == "" and button1.GetLabel() == "":
                    pass
                else:
                    #if button1.GetLabel() == "O":
                    noPlays.append(button3)

            elif button1.GetLabel() == button3.GetLabel() and button2.GetLabel() == "":
                if button1.GetLabel() == "" and button2.GetLabel() == "" and button1.GetLabel() == "":
                    pass
                else:
                    noPlays.append(button2)

            elif button2.GetLabel() == button3.GetLabel() and button1.GetLabel() == "":
                if button1.GetLabel() == "" and button2.GetLabel() == "" and button1.GetLabel() == "":
                    pass
                else:
                    noPlays.append(button1)

            noPlays = list(set(noPlays))

            if button1.GetLabel() == "" and button1 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button1)

            if button2.GetLabel() == "" and button2 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button2)

            if button3.GetLabel() == "" and button3 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button3)


        computerPlays = list(set(computerPlays))
        print(noPlays)
        choices = len(computerPlays)
        while 1 and computerPlays:
            btn = random.choice(computerPlays)

            if btn not in noPlays:
                print(btn.GetName())
                btn.SetLabel("O")
                btn.Disable()
                break
            else:
                print("Removed => " + btn.GetName())
                computerPlays.remove(btn)
            if choices < 1:
                self.giveUp()
                break
            choices -= 1
        else:
            # Окончание игры, если игрок победил
            self.giveUp()

        self.endTurnBtn.Disable()
        self.enableUnusedButtons()

    def giveUp(self):
        """
        Компьютер не может найти ход, чтобы обыграть игрока
        """
        msg = "Я сдаюсь. Хочешь сыграть ещё раз?"
        dlg = wx.MessageDialog(None, msg, "Игра закончена!",
                               wx.YES_NO | wx.ICON_WARNING)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            self.restart()
        else:
            wx.CallAfter(self.GetParent().Close)
        dlg.Destroy()

    def onRestart(self, event):
        """
        Рестарт
        """
        self.restart()

    def onToggle(self, event):
        """
        Отмечает выбранную кнопку крестом и отключает другие кнопки, если
        игрок не передумал
        """
        button = event.GetEventObject()
        button.SetLabel("X")
        button_id = button.GetId()

        self.checkWin()
        if not self.toggled:
            self.toggled = True
            self.endTurnBtn.Enable()
            for btn in self.widgets:
                if button_id != btn.GetId():
                    btn.Disable()
        else:
            self.toggled = False
            self.endTurnBtn.Disable()
            button.SetLabel("")
            self.enableUnusedButtons()

        # Ничья
        if not self.playerWon:
            labels = [True if btn.GetLabel() else False for btn in self.widgets]
            if False not in labels:
                msg = "Ничья. Хочешь сыграть ещё раз?"
                dlg = wx.MessageDialog(None, msg, "Игра закончена!",
                                       wx.YES_NO | wx.ICON_WARNING)
                result = dlg.ShowModal()
                if result == wx.ID_YES:
                    self.restart()
                dlg.Destroy()

    def restart(self):
        """
        Перезапускает игру и ресетает все кнопки
        """
        for button in self.widgets:
            button.SetLabel("")
            button.SetValue(False)
            button.SetBackgroundColour(self.normalBtnColour)
        self.toggled = False
        self.playerWon = False
        self.endTurnBtn.Disable()
        self.enableUnusedButtons()

class KRFrame(wx.Frame):
    #Frame

    def __init__(self):
        title = "Крестики-нолики"
        size = (500, 500)
        wx.Frame.__init__(self, parent=None, title=title, size=size)
        panel = KRPanel(self)

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = KRFrame()
    app.MainLoop()

