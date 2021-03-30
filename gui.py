import PySimpleGUI as sg
import ssh

sg.theme('BluePurple')

layout = [[sg.Text('Please press one of the following two buttons to query the data')],
          [sg.Button('Show top 10 Most Popular Movies')],
          [sg.Button('Show ten worst rated movies')],
          [sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show Most Popular Movies':
        ssh.launchFileThroughSSHpopular()
        
    if event == 'Show ten worst rated movies':
        ssh.launchFileThroughSSHrating()


window.close()