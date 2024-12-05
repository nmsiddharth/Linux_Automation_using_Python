import subprocess


def ps_cmd():
    result = subprocess.Popen(['wsl','ps','-ef'],stdout=subprocess.PIPE,text=True)

    while True:
        out = result.stdout.readline()
        if out:
            print(out.strip())

ps_cmd()