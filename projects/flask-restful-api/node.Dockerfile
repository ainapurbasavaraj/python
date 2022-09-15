FROM centos:centos7

RUN yum -y update && \
    yum -y install python3 epel-release python3-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . ./app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
