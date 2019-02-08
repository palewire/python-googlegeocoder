.PHONY: test ship

test:
	flake8 googlegeocoder
	coverage run test.py
	coverage report -m

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing
