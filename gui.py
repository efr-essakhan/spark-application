import PySimpleGUI as sg
import ssh

sg.theme('BluePurple')

layout = [[sg.Text('Please press one of the following two buttons to query the data')],
          [sg.Button('Show top 10 Most Popular Movies')],
          [sg.Button('Show ten worst rated movies')],
          [sg.Button('Exit')]]

window = sg.Window('Essa Khan CS3800 application', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show top 10 Most Popular Movies':
        #window['-OUTPUT-'].update(ssh.launchFileThroughSSHpopular())
        #ScrolledTextBox(ssh.launchFileThroughSSHpopular())
        sg.popup('Results:', "Movie name | Total number of ratings\n", ssh.launchFileThroughSSHpopular(), title = 'top 10 Most Popular Movies', non_blocking = True)
        #sg.ScrolledTextBox(ssh.launchFileThroughSSHpopular())
        #sg.popup_scrolled(ssh.launchFileThroughSSHpopular(), non_blocking = True)
        
    if event == 'Show ten worst rated movies':
        #ssh.launchFileThroughSSHrating()
        #sg.popup('Results:', "Movie name: Total number of ratings\n", ssh.launchFileThroughSSHrating(), title = 'top 10 Most Popular Movies', non_blocking = True)
        sg.popup_scrolled("Movie name | Tot. Num. of people that left rating | Avg. rating\n",ssh.launchFileThroughSSHlowestPopularRating, title = 'top 10 Most Popular Movies', non_blocking = True)

window.close()