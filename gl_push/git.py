import subprocess


def run(path, *cmd):
    return subprocess.run(["git"] + list(cmd), cwd=path, check=True)
