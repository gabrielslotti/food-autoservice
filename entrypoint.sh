#!/bin/sh

# Run migrations
poetry run alembic upgrade head

# Start the application
poetry run python src/main.py
