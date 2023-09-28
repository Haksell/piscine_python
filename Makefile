END := \033[0m
GREEN := \033[32m

test:
	@flake8 --ignore=D100 --exclude=test_*.py
	@echo "$(GREEN)✓ flake8$(END)"
	@mypy --ignore-missing-imports .
	@echo "$(GREEN)✓ mypy$(END)"
	@pytest
	@echo "$(GREEN)✓ pytest$(END)"

clean:
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf day0/ex09/build
	rm -rf day0/ex09/dist
	rm -rf day0/ex09/ft_package.egg-info
