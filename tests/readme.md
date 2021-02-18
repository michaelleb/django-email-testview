## How to run this test application
1.  start cdm ( shell ) in directory that contain manage.py
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. `python manage.py runserver`
1. expect that server is running on port 8000, which is the default port.

1. in browser, go to localhost:8000/admin
1. login with username: admin, password: admin
1. go to localhost:8000/admin/emails
1. expect to see one link to email 'dummy_app.dummy_email'
1. click on that link to view rendered email
1. feel free to add more email functions and methods to prevew in admin 

__Tested with Django==3.0.5__ 