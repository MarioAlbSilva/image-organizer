import PySimpleGUI as sg


# create layout
def layout():
    files_frame = [[sg.Radio('Copy Files', 'MOVE', default=True),
                    sg.Radio('Move Files', 'MOVE', key='-MOVE-')]]

    organize_frame = [[sg.Radio('First Letter', 'ORGANIZE', default=True,),
                       sg.Radio('Creation Date', 'ORGANIZE', key='-DATE-')]]

    gui = [[sg.Text('Photos Location', justification="right")],
           [sg.InputText(key='-PHOTOS-', readonly=True),
            sg.FolderBrowse()],
           [sg.Text('Destination Location')],
           [sg.InputText(key='-DESTINATION-', readonly=True),
            sg.FolderBrowse()],
           [sg.Frame('Files', files_frame),
            sg.Frame('Organize Files', organize_frame)],
           [sg.Output(size=(100, 5))],
           [sg.Button('Run', key='-RUN-')]]

    return gui


def organize_files(move_files):
    print('Start process')


def main():
    # Create the Window
    window = sg.Window('Photos', layout(), resizable=True)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

        if event == '-RUN-':
            organize_files(values['-MOVE-'])

if __name__ == '__main__':
    main()
