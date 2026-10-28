#!/usr/bin/env python3
"""Selector feature preservation and explicit runtime-profile checks; no API call."""
import unittest
from unittest.mock import Mock,patch
from imagen_mcp.providers.selector import ProviderSelector
from imagen_mcp import server
class Gate(unittest.TestCase):
    def test_explicit_provider_pin_cannot_fall_back(self):
        selector=ProviderSelector()
        with self.assertRaises(ValueError):selector.suggest_provider('Fictional landscape',explicit_provider='gemini',available_providers=['openai'])
    def test_reference_requirement_cannot_be_dropped(self):
        selector=ProviderSelector()
        with self.assertRaises(ValueError):selector.suggest_provider('Fictional packaging mockup',reference_images=['fictional.png'],available_providers=['openai'])
    def test_environment_runtime_does_not_load_dotenv(self):
        with patch.dict('os.environ',{'IMAGEN_MCP_CONFIG_PROFILE':'environment','IMAGEN_MCP_TRANSPORT':'stdio'}),patch('src.config.dotenv.load_dotenv') as loader,patch.object(server.mcp,'run') as run:
            server.main();loader.assert_not_called();run.assert_called_once_with()
if __name__=='__main__':unittest.main(verbosity=2)
