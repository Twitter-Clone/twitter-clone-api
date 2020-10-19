# twitter-clone-api
![twitter-clone-api](https://github.com/Twitter-Clone/twitter-clone-api/workflows/twitter-clone-api/badge.svg)
![](https://img.shields.io/github/issues/Twitter-Clone/twitter-clone-api)
![](https://img.shields.io/github/issues-closed/Twitter-Clone/twitter-clone-api)

### How to run API locally
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

### Deploying API on Server
Build the image with a tag
```
docker build -t backend:latest .
```

Run the docker image exposing port 8000
```
docker run -d -p 8000:8000 backend:latest
```

Navigate to this [link](http://157.245.160.185:8000/api/posts) to see all our Twitter posts.
