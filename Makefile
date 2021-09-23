run:
	docker run -p 5900:5900 -v C:\Users\Data\Desktop\docker-selenium-trunk\testFfmpeg_py2:/usr/src/app/  --name selenium_ffmpeg_1 selenium_ffmpeg
build:
	docker build . -t selenium_ffmpeg
