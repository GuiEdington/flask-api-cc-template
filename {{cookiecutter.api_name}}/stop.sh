#!/bin/bash

docker kill {{cookiecutter.api_name}}
docker rm {{cookiecutter.api_name}}