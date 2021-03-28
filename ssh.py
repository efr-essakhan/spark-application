import spur

shell = spur.SshShell(hostname="127.0.0.1", port=2222, username="maria_dev", password="maria_dev", missing_host_key=spur.ssh.MissingHostKey.accept)

with shell:
    # result = shell.run(["echo", "-n", "hellvbnbvno"])
    #result = shell.run(["echo", "-n", "hello"])
    #result = shell.run(["ls"])
    result = shell.run(["spark-submit", "LowestRatedMovieDataFrame.py"])
print(result.output.decode('utf-8')) # prints hello