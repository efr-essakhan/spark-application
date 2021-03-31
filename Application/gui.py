import PySimpleGUI as sg
import ssh

sg.theme('BluePurple')

layout = [[sg.Text('Please press one of the following two buttons to query the data')],
          [sg.Button('Show top ten worst rated movies')],
          [sg.Button('Show top ten worst rated movies with >= 10 total ratings')],
          [sg.Button('Show top 10 Most Popular Movies')],
          [sg.Button('Exit')]]

window = sg.Window('Essa Khan CS3800 application', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Show top ten worst rated movies':
        sg.popup_scrolled("Movie name | Tot. Num. of people that left rating | Avg. rating\n", ssh.launchFileThroughSSHlowestRating(), title = 'Top ten worst rated movies', non_blocking = True, location=(20, 20))
        
    if event == 'Show top ten worst rated movies with >= 10 total ratings':
        sg.popup_scrolled("Movie name | Tot. Num. of people that left rating | Avg. rating\n", ssh.launchFileThroughSSHlowestPopularRating(), title = 'Top ten worst rated movies with >= 10 total ratings', non_blocking = True, location=(10,10))

    if event == 'Show top 10 Most Popular Movies':
        sg.popup_scrolled('Results:', "Movie name | Total number of ratings\n", ssh.launchFileThroughSSHpopular(),
                 title='top 10 Most Popular Movies', non_blocking=True, location=(0,0))
window.close()