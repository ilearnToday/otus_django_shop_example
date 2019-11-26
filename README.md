# django shop example
Simple django application with main page and product page. Otus homework.
## Installation
###Clone project:
```bash
git clone https://github.com/ilearnToday/otus_django_shop_example.git
```
### Set up environment:
You can find instructions [here](https://docs.python.org/3.6/library/venv.html)

### Install requrements
```bash
pip install -r requirements.txt
```
###Set up secret key for project:
* Generate key 
```bash
python -c 'import random;
result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]);
print(result)'
```
* Add SECRET KEY to secret.py file or env on your machine
* Import it in settings
 
## To run local server use:
```bash
python3 manage.py runserver
```
## Requirements
```Django==2.2.5```
```django-configurations==2.1```
```Python>=3.6.8```