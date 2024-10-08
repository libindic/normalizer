test:
	coverage run --source=libindic -m unittest discover -s libindic

travis: test

clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
	rm -rf build dist *egg* .tox .coverage .testrepository
