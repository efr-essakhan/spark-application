import PySimpleGUI as sg
import spur

def SSHstuff():
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev",
                          missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        #Storing u.data into HDFS cluster
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/ml-100k/u.data"])
        #shell.run(["hadoop", "fs", "-rm", "-r", "ml-100k"])
        shell.run(["hadoop", "fs", "-mkdir", "ml-100k"])
        shell.run(["hadoop", "fs", "-copyFromLocal", "u.data", "ml-100k/u.data"])
        shell.run(["rm", "u.data"])
        
        #Storing u.item onto local
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/ml-100k/u.item"])
        #shell.run(["rm", "-r", "ml-100k"])
        shell.run(["mkdir", "ml-100k"])
        shell.run(["mv", "u.item" ,"ml-100k"])
        
        #Storing Spark Scripts onto local
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/LowestRatedMovie.py"])
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/LowestRatedPopularMovie.py"])
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/PopularMovie.py"])
        
sg.theme('BluePurple')

layout = [[sg.Text('Please press the button below to auto download necessary files and configure your Hortonworks sandbox')],
          [sg.Text('Once you press the Start button please wait patiently until a pop-up shows confirming process completion (takes less than 2 minutes ussually)')],
          [sg.Button('Start')]]

window = sg.Window('CS3800: Auto Configure Hortonworks sandbox application', layout)

while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED:
        break

    if event == 'Start':
        SSHstuff()
        sg.popup("Finished!", title = 'Message')



        

