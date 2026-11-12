# stacktally
A service catalog and policy engine for Docker Compose environments. It keeps one declared source of truth per service, detects drift between what's declared, what's in the compose files, what's actually running, and what monitoring knows about.

## Development

  uv sync
  uv run pytest
  uv run ruff check