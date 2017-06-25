import gl_push
import gl_push.git
import gl_push.gitlab

from unittest import mock


def test_push(git_server, monkeypatch, tmpdir):
    url = git_server.create_repo("foo/bar")
    monkeypatch.chdir(tmpdir)
    foo_dir = tmpdir.ensure_dir("foo")
    gl_push.git.run(foo_dir, "clone", url)
    bar_src = foo_dir.join("bar")
    bar_src.join("README").write("This is the README")
    gl_push.git.run(bar_src, "add", ".")
    gl_push.git.run(bar_src, "commit", "--message", "Initial commit")
    gl_push.git.run(bar_src, "push", "origin", "master:master")
    gl_push.git.run(bar_src, "checkout", "-b", "test1")
    gl_push.git.run(bar_src, "commit", "--message", "test", "--allow-empty")

    with mock.patch("gl_push.gitlab") as mock_gitlab:
        monkeypatch.chdir(bar_src)
        gl_push.main()
        mock_gitlab.ensure_merge_request.assert_called_with(
            "foo/bar",
            "test1",
            title="test1"
        )
