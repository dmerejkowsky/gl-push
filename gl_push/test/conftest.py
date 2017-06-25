import pytest

from gl_push.test.git_server import GitServer


@pytest.fixture
def git_server(tmpdir):
    return GitServer(tmpdir)
