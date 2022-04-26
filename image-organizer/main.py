import os
import shutil
import PySimpleGUI as sg


# create layout
def layout():
    files_frame = [[sg.Radio('Copy Files', 'MOVE', default=True),
                    sg.Radio('Move Files', 'MOVE', key='-MOVE-')]]

    # organize_frame = [[sg.Radio('First Letter', 'ORGANIZE', key='-LETTER-', default=True,),
    #                   sg.Radio('Creation Date', 'ORGANIZE', key='-DATE-')]]

    gui = [[sg.Text('Photos Location', justification="right")],
           [sg.InputText(key='-PHOTOS-', readonly=True),
            sg.FolderBrowse()],
           [sg.Text('Destination Location')],
           [sg.InputText(key='-DESTINATION-', readonly=True),
            sg.FolderBrowse()],
           [sg.Frame('Files', files_frame)],
           [sg.Multiline(size=(100, 5), disabled=True, autoscroll=True, reroute_stdout=True, reroute_stderr=True)],
           [sg.Button('Run', key='-RUN-')]]

    return gui


def organize_files(move_files: bool, files_folder: str, destination_folder: str):
    print('Start process')
    type_operation = 'Move files ' if move_files else 'Copy files'
    print(f'{type_operation} from {files_folder} to {destination_folder}')

    characters_list = ['/', '#', '-', '_']
    included_extensions = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
    file_names = [fn for fn in os.listdir(files_folder)
                  if any(fn.endswith(ext) for ext in included_extensions)]

    for file in file_names:
        letter = file[0].upper()

        # if first letter is a number or character in list use # as folder name
        if letter.isnumeric() or letter in characters_list:
            letter = '#'

        folder = destination_folder + '/' + letter

        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f'create folder {folder}')

        if move_files:
            shutil.move(files_folder + '/' + file, folder)
        elif not move_files:
            shutil.copy2(files_folder + '/' + file, folder)

        print(f'{file} to {folder}')

    print('process finished')


def main():
    # Create the Window
    window = sg.Window('Photos', layout(), resizable=True)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

        if event == '-RUN-':
            files_folder = values['-PHOTOS-']
            destination_folder = values['-DESTINATION-']

            if len(files_folder) == 0:
                sg.Popup('Photos folder not select')
                continue

            if len(destination_folder) == 0:
                sg.Popup('Destination folder not select')
                continue

            organize_files(values['-MOVE-'], files_folder, destination_folder)


if __name__ == '__main__':
    main()
