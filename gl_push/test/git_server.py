import gl_push.git


class GitServer():
    def __init__(self, tmpdir):
        self.root = tmpdir.join("srv").mkdir()

    def create_repo(self, name):
        dest = self.root.ensure_dir(name)
        gl_push.git.run(dest, "init", "--bare")
        return dest
