import subprocess


def df_cmd():
    try:
        result = subprocess.run(['wsl','df','-hT'],capture_output=True,text=True,check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)

df_cmd()