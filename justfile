# List all available recipes
default:
	just --list

# Run checks (ruff + black)
check:
	ruff spotifinder
	black --check spotifinder

# Automatically fix all formating (ruff + black)
format:
	black spotifinder
	ruff --fix spotifinder
