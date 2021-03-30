import spur

def launchFileThroughSSHrating():
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev",
                          missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        result = shell.run(["spark-submit", "LowestRatedPopularMovieDataFrame.py"])
    print(result.output.decode('utf-8'))  # prints hello

def launchFileThroughSSHpopular():
    shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev",
                          missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        result = shell.run(["spark-submit", "PopularMovie.py"])
    print(result.output.decode('utf-8'))  # prints hello

