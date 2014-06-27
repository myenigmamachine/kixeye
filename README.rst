=====
Kixeye Support
=====

A customer support system for a fictional online game.

Quick start
-----------

1. Add "support" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'support',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^support/', include('support.urls')),

3. Run the below commands to create a certificate for HTTPS/SSL support

openssl genrsa -out kixeye.key 2048
openssl req -new -key kixeye.key -out kixeye.csr
openssl x509 -req -days 365 -in kixeye.csr -signkey kixeye.key -out kixeye.crt

3. Run `uwsgi --master --https 0.0.0.0:8000,kixeye.crt,kixeye.key --wsgi-file kixeye/wsgi.py` to run the app.

4. Start the development server and visit https://localhost:8000/admin/
   to create a user (you'll need the Admin app enabled).

5. Visit https://localhost:8000/users/ to participate in the poll.
