test:
	@flake8 --ignore=D100 --exclude=test_*.py
	@pytest -rA -vv

clean:
	@rm -rf `find . -type d -name .pytest_cache`
	@rm -rf `find . -type d -name __pycache__`
	@git clean -xdf
