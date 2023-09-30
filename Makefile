dist:
	python3 -m build

upload:
	python3 -m twine upload --repository testpypi dist/* --config-file=~/.pypirc --non-interactive
