all:
	flake8
	pytest -rA -vv

clean:
	rm -rf */*/__pycache__