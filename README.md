# SimplifyReport📢

### About the Project
SimplifyReport is an Android Application with backend on Django REST Framework which simplifies the process of reporting cases of fire 🧯, crimes⚠️ and calling an ambulance🚑.
Immediate help is provided to people in cases of emergencies as these. User can easily post his reports and his neighbours are immediately notified through the application in cases of emergency such as fire outbreak, robbery or any other crime. 

This repository contains the REST APIs of the application.
> **Deployed APIs can be found [here](https://simplify-reports.herokuapp.com/).**

 ### API Endpoints
 - Creating User Profile - GET, PUT and POST request
```
https://simplify-reports.herokuapp.com/profile/
```
- For User Login
```
http://127.0.0.1:8000/rest-auth/login/
```
- Making fire reports - GET and POST request
```
https://simplify-reports.herokuapp.com/fire/
```
- Making police reports - GET and POST request
```
https://simplify-reports.herokuapp.com/police/
```
- Calling ambulance - GET and POST request
```
https://simplify-reports.herokuapp.com/ambulance/
```
 
 
### Quick Start

- Fork and Clone the repository using-
```
git clone https://github.com/AbsurdNerd/SimplifyReport_Backend
```
- Create virtual environment-
```
python -m venv env
Mac OS / Linux:
source env\Scripts\activate
Windows:
env\Scripts\activate
```
- Install dependencies using-
```
pip install -r requirements.txt
```
- Make migrations using-
```
python manage.py makemigrations
```
- Migrate Database-
```
python manage.py migrate
```
- Create a superuser-
```
python manage.py createsuperuser
```
- Run server using-
```
python manage.py runserver
```
- Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in the browser.


### Our Team 😄:

| S.No. | Name               | Role                      | GitHub Username :octocat:                              |
| ----- | ------------------ | ------------------------- | ----------------------------------------------------   |
| 1.    | Dheeraj Kotwani    | Android Developer         | [@dheerajkotwani](https://github.com/dheerajkotwani)   |
| 2.    | Vatsal Kesarwani   | Android Developer         | [@plazzy99](https://github.com/plazzy99)               |
| 3.    | Diya Jaiswal       | Backend Developer         | [@diyajaiswal11](https://github.com/diyajaiswal11)     |
| 4.    | Manshi Todi        | Backend Developer         | [@todi-2000](https://github.com/todi-2000)             |

## Contributors ✨:

<a href="https://github.com/AbsurdNerd/SimplifyReport_Backend/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AbsurdNerd/SimplifyReport_Backend" />
</a>

