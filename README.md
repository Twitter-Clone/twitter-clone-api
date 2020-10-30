# twitter-clone-api
![twitter-clone-api](https://github.com/Twitter-Clone/twitter-clone-api/workflows/twitter-clone-api/badge.svg)
![](https://img.shields.io/github/issues/Twitter-Clone/twitter-clone-api)
![](https://img.shields.io/github/issues-closed/Twitter-Clone/twitter-clone-api)

## How to run API locally
Start up virtual machine
```
python3 -m venv env
source env/bin/activate
```

Install Dependencies
```
pip3 install -r requirements.txt
```

Run API server
```
python3 manage.py runserver
```

## Deploying API on Server
Build the image with a tag
```
docker build -t backend:latest .
```

Run the docker image exposing port 8000
```
docker run -d -p 8000:8000 backend:latest
```

## Running Unit Tests with Django Testing
The `--keepdb` will re-use the previous database built and `--parallel` will run all tests in parallel   
of each other. `v 2` displays more detail for the test cases.
```
python3 manage.py test --keepdb --parallel v 2
```

Navigate to this [link](http://157.245.160.185:8000/api/posts) to see all our Twitter posts as JSON data.  
Navigate to this [link](http://157.245.160.185:8000/api/users) to see all our Twitter users as JSON data.
