import subprocess


def run(path, *cmd, capture=False):
    stdout = subprocess.PIPE if capture else None
    return subprocess.run(["git"] + list(cmd), cwd=path, check=True,
                          stdout=stdout)
