import PySimpleGUI as sg
import spur


def launchFileThroughSSHlowestRating():
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev",
                          missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        #Storing u.data into HDFS cluster
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/ml-100k/u.data"])
        shell.run(["hadoop", "fs", "-mkdir", "ml-100k"])
        shell.run(["hadoop", "fs", "-copyFromLocal", "u.data", "ml-100k/u.data"])
        shell.run(["rm", "u.data"])
        
        #Storing u.item onto local
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/ml-100k/u.item"])
        shell.run(["mkdir", "ml-100k"])
        shell.run(["mv", "u.item" ,"ml-100k"])
        
        #Storing Spark Scripts onto local
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/LowestRatedMovie.py"])
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/LowestRatedPopularMovie.py"])
        shell.run(["curl", "-O", "https://raw.githubusercontent.com/essakh/spark-application/master/Spark%20files/PopularMovie.py"])
        
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="root", password="hadoop",
                          missing_host_key=spur.ssh.MissingHostKey.accept)
    with shell:
        #Installing python
        shell.run(["yum", "install", "python-pip"])

launchFileThroughSSHlowestRating()