# The shop - The CRM
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/Python-v3.12-blue?logo=python)](https://www.python.org/)
[![Django 3.2.25](https://img.shields.io/badge/Django-v3.2.25-darkgreen?logo=django)](https://www.djangoproject.com/)

## Description 
This project was created as part of my studies and as an example project for my portfolio in 2023. The process of creating the project has been recorded in videos and published on my YouTube channel. Links to the videos:
- [ESpace #1: Simple Login by Django Base User ](https://www.youtube.com/watch?v=3DttOh2KofU)
- [ESpase #2: Login Template Show info from Database Add info to the Database](https://www.youtube.com/watch?v=TvR7L9K2T_Q&pp=0gcJCSgLAYcqIYzv)
- [ESpace #3: Creating a Shop app, the home page, show products from the database, use shop template](https://www.youtube.com/watch?v=bSOAe3e79Lg)

## Project structure
The project consists of two parts:
- Shop (Clients side)
- Dashboard (Employments side)

## Project setup
### Add environment
```
python3 -m venv venv
```

### Activate environment
```
source venv/bin/activate 
```

### Install requirements
```
pip install -r requirements.txt
```

### Migrate models
```
python3 manage.py migrate
```
> Prepared the SQLite DB there is in the repository

### Run server
```
python3 manage.py runserver
```

### Page address
[http://localhost:8000](http://localhost:8000)

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Preview images
#### Shop
![the_shop-the_crm-home.png](example__simple_shop/static/example__simple_shop/img/the_shop-the_crm-home.png)

![the_shop-the_crm-goods-card.png](example__simple_shop/static/example__simple_shop/img/the_shop-the_crm-goods-card.png)

#### Dashboard
![the_shop-the_crm-dashboard.png](example__simple_shop/static/example__simple_shop/img/the_shop-the_crm-dashboard.png)
