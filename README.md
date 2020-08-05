# Flask API CookieCutter Template
A CookieCutter template of a simple Flask WebAPI application.

## How to Create your new API

First you need to get CookieCutter (here: https://cookiecutter.readthedocs.io/en/1.7.2/installation.html, try it using pip, it's the easiest way :D).

Then run:
```bash
cd ..
cookiecutter flask-api-cc-template
```

You'll be asked to enter the name of the new API project (pressing ENTER causes it to use the default).

And your new API is ready to go!

## How to run

You'll need to have Docker installed in your machine: https://docs.docker.com/get-docker/

Then, simply run:

```bash
cd MY_API_FOLDER
bash start.sh
```
Now, open it in your browser http://localhost:8080/

To stop the API, just run:

```bash
bash stop.sh
```
