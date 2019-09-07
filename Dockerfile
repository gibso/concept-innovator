FROM python:3

# add workdir for project
RUN mkdir /opt/project
WORKDIR /opt/project

# copy all files
COPY . .

# install dependencies
RUN  pip3 install -e .

# start flask server
CMD flask run --host=0.0.0.0
