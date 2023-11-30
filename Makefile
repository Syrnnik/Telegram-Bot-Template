IMAGE_NAME=your-image-name:your-tag

install:
	pip3 install -r requirements.txt

run:
	python3 src/main.py

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run --rm -it --env-file .env -p 8080:8080 -v ${CURDIR}/src:/app/src $(IMAGE_NAME)
