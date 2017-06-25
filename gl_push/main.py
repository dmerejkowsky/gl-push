import os

import gl_push.git
import gl_push.gitlab


def main():
    cwd = os.getcwd()
    res = gl_push.git.run(cwd, "remote", "get-url", "origin",
                          capture=True)
    project = "/".join(res.stdout.decode().strip().split("/")[-2:])

    res = gl_push.git.run(cwd, "rev-parse", "--abbrev-ref", "HEAD",
                          capture=True)
    branch = res.stdout.decode().strip()

    title = branch
    gl_push.gitlab.ensure_merge_request(project, branch, title=title)
