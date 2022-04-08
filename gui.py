import PySimpleGUI as sg
from upAndDown import UpAndDown


class MyGUI():
    def __init__(self):
        self.up_down=UpAndDown()

    def run(self):
        sg.theme('DarkAmber')

        layout = [ 
                    [sg.Text('Enter something on Row 2'), sg.InputText()],
                    [sg.Button('Ok'), sg.Button('Cancel')],
                    [sg.Multiline(size=(30, 5), key='textbox')], ]


        window = sg.Window('Window Title', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            uad_text=self.up_down.arrange(values[0])
            window['textbox'].Update(uad_text)
            print('You entered ', uad_text)

        window.close()


if __name__ == '__main__':
    gui=MyGUI()
    gui.run()
