version := 1.2.0

build:
	python -m build .

upload: build
	twine3 upload -s dist/discid-$(version).tar.gz

check:
	pytest --verbose

disccheck:
	PYTHON_DISCID_TEST_DEVICE=1 pytest --verbose

doc:
	cd doc && make dirhtml

version:
	sed -i -e 's/\(__version__\s=\s"\)[0-9.]\+[0-9a-z.-]*/\1$(version)/' \
		discid/__init__.py
	sed -i -e 's/\(version = "\)[0-9.]\+[0-9a-z.-]*/\1$(version)/' \
		pyproject.toml

clean:
	rm -f *.pyc discid/*.pyc
	rm -rf __pycache__ discid/__pycache__

.PHONY: doc build
