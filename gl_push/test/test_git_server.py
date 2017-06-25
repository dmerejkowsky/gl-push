import gl_push.git
from gl_push.test.git_server import GitServer


def test_can_create_a_repo(tmpdir, monkeypatch):
    server = GitServer(tmpdir)
    url = server.create_repo("foo")
    monkeypatch.chdir(tmpdir)
    gl_push.git.run(tmpdir, "clone", url)
    assert tmpdir.join("foo").exists()
