all:
	flake8
	pytest -rA -vv

clean:
	@rm -rf `find . -type d -name .pytest_cache`
	@rm -rf `find . -type d -name __pycache__`
