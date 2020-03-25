# Fact boy

## Table of Contents
- [About the Repo](#about-the-repo)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Code Structure](#code-structure)
- [Tech](#tech)
- [Contributors](#contributors)

## About the Repo
Fact boy is useful tool linked to the Wikipedia API to provide users with interesting facts.

## Prerequisites
- pip
- virtualenv

## Getting Started
Navigate to the project folder and create the virtual environment using:

virtualenv [environment name]

Then, active the virtual environment that was just created using:

source /env/bin/activate

We then need to install the requirements for the project using:

pip install -r requirements.txt

Finally we can run the project with:

python app.py

## Code Structure
This is the general project structure
```
.
├── static
|   ├── main.js
|   ├── normalize.css
|   ├── skeleton.css
|   ├── styles.css
├── templates
|   ├── index.html
|   ├── layout.html
├── app.py
├── config.py
├── LICENSE
├── README.md
├── requirements.txt

```

## Tech
- [Flask](https://github.com/pallets/flask)
- [Skeleton.css](http://getskeleton.com/)

## Contributors
- Eros Di Pede
  + [Github](https://github.com/ForkBombGIT)
  + [Website](https://erosdipede.me/)
