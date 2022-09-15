To build image : docker build -f node.Dockerfile -t flask-restful .

To run container  : docker run -p 5000:5000 -v $(pwd):/app/ flask-restful

To test the application, Use Flask_restful from  postman collection in this folder


##################################################
Flask-restful is a wrapper on Flask which implements routes like GET, POST and its based on the resource

Flask-JWT - is a JSON web token, 
