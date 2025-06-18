# Django

Python Web Framework

[Documentation](https://docs.djangoproject.com/en/5.0/)

## Install Django

[Tutorial](https://docs.djangoproject.com/en/5.0/topics/install/#how-to-install-django)

On production, use Apache with mod_wsgi
- Web servers dont natively speak Python, we need an interface to make that communication happen
  - [WSGI](https://wsgi.readthedocs.io/en/latest/) is the main Python standard
  - [ASGI](https://asgi.readthedocs.io/en/latest/) is the new async friendly standard (allows site to use async Python and Django features)

## Deploy Django

[Tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04)

### Edit sites-available

- WSGIDaemonProcess name-of-your-project python-home=/path/to/venv python-path=/path/to/folder/with-manage.py
- WSGIScriptAlias / (route to url) /path/to/wsgi.py