#!/bin/bash

docker build -t {{cookiecutter.api_name}} .

docker run -itd -p 8080:5000 {{cookiecutter.api_name}}  
