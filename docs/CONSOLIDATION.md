# Local capability consolidation — 2026-10-28

Generate images through one provider interface while preserving explicit feature requirements.

Public catalog name: **Imagen Provider** (`amplifier-tool-imagen-provider`). The retained native distribution, Python import and CLI identities stay unchanged. This branch is a reviewable local consolidation; no remote rename or publication has happened.

Provider invocation can cost money and requires an approved environment credential. Selector/mock tests do not generate images.

The parked video-mcp stub is retained separately as reference; it is not advertised as a functioning video provider.

Server defaults to environment-only configuration; IMAGEN_MCP_CONFIG_PROFILE=local explicitly enables the retained dotenv setup profile.

The original source guide remains below the new README front door. Test fixtures and dry runs are not actual provider, invitation, film or deployment acceptance. Full history, engines and licenses remain in this owner repository.

For the MCP server, the default `IMAGEN_MCP_CONFIG_PROFILE=environment` reads runtime values from the environment. Users who intentionally rely on the historical local .env file can set `IMAGEN_MCP_CONFIG_PROFILE=local`; it never overrides existing environment values. The interactive setup CLI retains its explicit local credential setup flow. No credential values are printed in the new tests.
