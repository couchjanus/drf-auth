# REST APIs
## Install package[(https://django-rest-auth.readthedocs.io/en/latest/installation.html)]:
```
pip install django-rest-auth
```
Add rest_auth app to INSTALLED_APPS in your django settings.py:
```
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'rest_auth'
)
```
This project depends on django-rest-framework library, so install it if you haven’t done yet. Make sure also you have installed rest_framework and rest_framework.authtoken apps

### Add rest_auth urls:
```
urlpatterns = [
    ...,
    url(r'^rest-auth/', include('rest_auth.urls'))
]
```
### Migrate your database
```
python manage.py migrate
```
You’re good to go now!

## Registration (optional)
If you want to enable standard registration process you will need to install django-allauth by using 
```
pip install django-rest-auth[with_social]
```
Add django.contrib.sites, allauth, allauth.account and rest_auth.registration apps to INSTALLED_APPS in your django settings.py:

### Add SITE_ID = 1 to your django settings.py
```
INSTALLED_APPS = (
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
)

SITE_ID = 1
```
Add rest_auth.registration urls:
```
urlpatterns = [
    ...,
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
```
## Links:
- Django REST Framework Course for Beginners [(https://codeloop.org/django-rest-framework-course-for-beginners/)]

- Django REST framework [(https://www.django-rest-framework.org/tutorial/quickstart/)]