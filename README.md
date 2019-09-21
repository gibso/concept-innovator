ORPHEUS SPECIFIER [![Build Status](https://travis-ci.com/gibso/orpheus-specifier.svg?branch=master)](https://travis-ci.com/gibso/orpheus-specifier)						
=================================

This project is part of the [Orpheus Application](https://github.com/gibso/orpheus-dev).

### Overview
This project extracts mental spaces for concepts from the [ConceptNet](http://conceptnet.io/) knowledge base, and specifies them in the algebraic CASL language.

### Endpoints

when running the server e.g. on http://localhost:3000, you can request the following endpoints:

 #### POST  http://localhost:5000/specify/concept

This Endpoint extracts a mental space for a given concept, and returns it in its CASL specification.
The endpoint expects the concept name as json form-data, e.g:
```
{
  "concept-name": "boat"
}
```

 #### POST  http://localhost:5000/generator/input-spaces

This Endpoint extracts the mental spaces for two given concepts, and returns its CASL specification.
This specification can serve as an input specification for the [amalgamation module](https://github.com/gibso/Amalgamation).
The endpoint expects the input space names as json form-data, e.g:
```
{
  "input-space-names": ["house", "boat"]
}
```


### Setup

clone this project by running 
```
git clone git@github.com:gibso/orpheus-specifier.git
```

and enter the directory: `cd orpheus-specifier`

#### Setup Using [docker](https://www.docker.com/get-started)
Build a docker image of the project by running
```
docker build -t orpheus-specifier .
```

Then you can start the flask server in a docker container by running
```
docker run --rm -it -p 3000:5000 orpheus-specifier
```
Now you can reach your server at http://localhost:3000 


#### Setup without docker
Python3 and virtualenv is required. Create a virtual python3 env and activate it:
```
virtualenv -p python3 venv && source venv/bin/activate
```
Now you can install the project requirements with 
```
pip install -e . 
```
Then you can start the flask server by running
```
flask run
```
Now you can reach your server at http://localhost:5000 

### Author
Oliver Görtz (oliver.goertz{at}gmail.com)