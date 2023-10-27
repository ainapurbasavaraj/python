To build image : docker build -f node.Dockerfile -t bainapur/webserver:tag .
To build platform specific image : docker build --platform linux/amd64 -f node.Dockerfile -t bainapur/webserver:tag .

To run container : docker run -p 5000:5000 -v $(pwd):/app/ bainapur/webserver:tag

To push images to registry : docker push bainapur/webserver:tag
