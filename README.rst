=====
Kixeye Support
=====

A customer support system for a fictional online game.

Quick start
-----------

1. Download code with "git clone https://github.com/myenigmamachine/kixeye.git"

2. cd kixeye

2. Install nessesary packages with "pip install -r kixeye/requirements.txt"

2. Install contained package with "python setup.py install"

3. Run the below commands to create a certificate for HTTPS/SSL support
   a. Note: Please install openssl first if it is not already installed on your machine

openssl genrsa -out kixeye.key 2048
openssl req -new -key kixeye.key -out kixeye.csr
openssl x509 -req -days 365 -in kixeye.csr -signkey kixeye.key -out kixeye.crt

3. Sync database with "python manage.py syncdb"
   a. Recommended: Create an admin user for testing

3. 

3. Run `uwsgi --master --https 0.0.0.0:8000,kixeye.crt,kixeye.key --post-buffering 1 --wsgi-file kixeye/wsgi.py` to run the app.

4. visit https://localhost:8000/admin/ to create a user (you'll need the Admin app enabled).

4. Explore the site

OPTIONAL:

4. Generate dummy database entries with "./scripts/populate_data.sh"
   a. Note: This script assumes a user with username "admin" and password "password" to populate data.

4. Run tests with "python manage.py test"
