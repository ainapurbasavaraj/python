To build image : docker build -f node.Dockerfile -t webserver .

To run container : docker run -p 5000:5000 -v $(pwd):/app/ webserver

To test the application, Use the postman project
