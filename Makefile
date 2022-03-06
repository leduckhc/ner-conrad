build:
	docker build -t ner-conrad:latest .

run:
	docker stop ner-conrad
	docker rm ner-conrad
	docker run --detach --name ner-conrad -p8000:8000 ner-conrad:latest

test:
	python -m pytest test_unit.py -sv

integration:
	python -m pytest test_integration.py -sv

all: test build run
