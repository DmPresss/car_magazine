# car_magazine
WebApp about cars.

### description: 
- this application will allow you to learn more about car,
- you can signin and add your post about cars with photo,
- Adding the posts and extended capabilities of WebApp will be available for authorized users only.
### technologies:

Python  3.8.10

Django==4.1.3

### preparation and installation of WebApp at the local host:

- clone the repository using SSH key

```
$ git clone git@...

```
- go to cloned directory 

```
$ cd car_magazine

```
- deploy the virtual environment

```
$ python3 -m venv venv

```
- activate the virtual environment:

```
$ source venv/bin/activate

```
- install all requirements parameters:

```
$ pip install -r requirements.txt

```
- go to root directory of the progect: 

```
$ cd carssite 

```
- carry out migrate

```
$ python3 manage.py migrate

```
- you can upload origin db.sqlite3 and apply it in the project

```
https://drive.google.com/file/d/1NmDLjMIiH8AMLaENM3oXl5dWCyvWABWj/view?usp=share_link

```
- runserver: 

```
$ python3 manage.py runserver

```
### Author
Dmitry Parkhomenko 