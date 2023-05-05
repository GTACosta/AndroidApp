import App.media
import pytest


class TestApp:
    @pytest.mark.xfail
    def test_se_o_app_esta_rodando(self):
        assert App.media.MediaApp.run(self)
