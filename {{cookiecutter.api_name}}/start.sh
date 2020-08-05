#!/bin/bash

docker build -t {{cookiecutter.api_name}} .

docker run -itd -p 8080:5000 --name {{cookiecutter.api_name}} {{cookiecutter.api_name}}  
