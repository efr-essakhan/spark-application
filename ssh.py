import spur

def launchFileThroughSSHlowestRating():
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev",
                          missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        result = shell.run(["spark-submit", "LowestRatedMovie.py"]) # LowestRatedPopularMovieDataFrame.py
    return result.output.decode('utf-8')

def launchFileThroughSSHlowestPopularRating():
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev",
                          missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        result = shell.run(["spark-submit", "LowestRatedPopularMovie.py"]) # LowestRatedPopularMovieDataFrame.py
    return result.output.decode('utf-8')



def launchFileThroughSSHpopular():
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev",
                          missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        result = shell.run(["spark-submit", "PopularMovie.py"])
    return result.output.decode('utf-8')

