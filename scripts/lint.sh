#!/bin/bash
set -x

uv run lint-imports

uv run ty check

uv run ruff check --fix