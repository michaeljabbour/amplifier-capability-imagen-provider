"""The server has an environment-only default; local dotenv setup is explicit."""

from unittest.mock import Mock

import pytest

from src import server


def test_default_server_does_not_read_local_dotenv(monkeypatch):
    loader = Mock()
    run = Mock()
    monkeypatch.setattr("src.config.dotenv.load_dotenv", loader)
    monkeypatch.setattr(server.mcp, "run", run)
    monkeypatch.delenv("IMAGEN_MCP_CONFIG_PROFILE", raising=False)
    monkeypatch.setenv("IMAGEN_MCP_TRANSPORT", "stdio")
    server.main()
    loader.assert_not_called()
    run.assert_called_once_with()


def test_local_profile_preserves_explicit_setup_mode(monkeypatch):
    loader = Mock()
    run = Mock()
    monkeypatch.setattr("src.config.dotenv.load_dotenv", loader)
    monkeypatch.setattr(server.mcp, "run", run)
    monkeypatch.setenv("IMAGEN_MCP_CONFIG_PROFILE", "local")
    monkeypatch.setenv("IMAGEN_MCP_TRANSPORT", "stdio")
    server.main()
    loader.assert_called_once_with(override=False)
    run.assert_called_once_with()


def test_unknown_profile_stops_before_server_run(monkeypatch):
    run = Mock()
    monkeypatch.setattr(server.mcp, "run", run)
    monkeypatch.setenv("IMAGEN_MCP_CONFIG_PROFILE", "unknown")
    with pytest.raises(ValueError, match="CONFIG_PROFILE"):
        server.main()
    run.assert_not_called()
