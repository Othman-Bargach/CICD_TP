# CI/CD TP

## Description

This is the source code for the CI/CD TP project.

## Content

The code is split in many parts

* The "frontend" : for the static website page in html/css/js
* The "backend" : for the api in python
* The "aws instance" : for the ec2 infrastructure written in terraform

### Front

The front is a very simple HTML page with a few JS components making HTTP requests to the back.

### Back

The back is a couple of Python files making HTTP requests to a [public Pokémon API](https://pokeapi.co/) to retrieve a random Pokémon. It also has a small Flask file that the front queries for the results. There is no database as of now, but it could be added if need be.

