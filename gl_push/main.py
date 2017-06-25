import os

import gl_push.git
import gl_push.gitlab


def main():
    cwd = os.getcwd()
    project = gl_push.git.get_project_name(cwd)
    branch = gl_push.git.get_current_branch(cwd)
    title = branch

    gl_push.gitlab.ensure_merge_request(project, branch, title=title)
