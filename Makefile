image:
	docker build -t smartmirror:latest .

run: stop image
	docker run -p 8000:8000 --name smartmirror-container smartmirror:latest

stop:
	docker stop smartmirror-container && docker rm smartmirror-container || true