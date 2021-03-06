import PySimpleGUI as sg
import ssh

sg.theme('BluePurple')

layout = [[sg.Text('This program should be used only after you have ran hortonworksSetup application once \n')],
          [sg.Text('Please press one of the following buttons to query the data')],
          [sg.Button('Show top ten worst rated movies')],
          [sg.Button('Show top ten worst rated movies with >= 10 rating submissions')],
          [sg.Button('Show top 10 Most Popular Movies')],
          [sg.Text('\n Once you press a button please wait patiently until a pop-up shows displaying the results (takes less than 3 minutes usually)')]]

window = sg.Window('Essa Khan CS3800 Main Application', layout)

while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED:
        break

    if event == 'Show top ten worst rated movies':
        #Call method to Submit respective spark script through SSH across cluster and display results in new pop-up window
        sg.popup_scrolled("Movie name | Tot. Num. of rating submissions | Avg. rating\n", ssh.launchFileThroughSSHlowestRating(), title = 'Top ten worst rated movies', non_blocking = True, location=(0, 0))
        
    if event == 'Show top ten worst rated movies with >= 10 rating submissions':
        #Call method to Submit respective spark script through SSH across cluster and display results in new pop-up window
        sg.popup_scrolled("Movie name | Tot. Num. of rating submissions | Avg. rating\n", ssh.launchFileThroughSSHlowestPopularRating(), title = 'Top ten worst rated movies with >= 10 rating submissions', non_blocking = True, location=(0,0))

    if event == 'Show top 10 Most Popular Movies':
        #Call method to Submit respective spark script through SSH across cluster and display results in new pop-up window
        sg.popup_scrolled("Movie name | Tot. Num. of rating submissions\n", ssh.launchFileThroughSSHpopular(),
                 title='Top 10 Most Popular Movies', non_blocking=True, location=(0,0))
window.close()