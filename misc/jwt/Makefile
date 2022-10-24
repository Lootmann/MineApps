run:
	python3 main.py

.PHONY: in
in:
	python3 main.py < in

.PHONY: watch
watch:
	find . | entr -c python3 main.py

.PHONY: test
test:
	pytest -sv
