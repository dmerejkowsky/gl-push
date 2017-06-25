import subprocess


def run(path, *cmd):
    return subprocess.run(["git"] + list(cmd), cwd=path, check=True)


def run_out(path, *cmd):
    res = subprocess.run(["git"] + list(cmd), cwd=path, check=True,
                         stdout=subprocess.PIPE)
    return res.stdout.strip().decode()


def get_project_name(path):
    url = run_out(path, "remote", "get-url", "origin")
    return "/".join(url.split("/")[-2:])


def get_current_branch(path):
    return run_out(path, "rev-parse", "--abbrev-ref", "HEAD")
