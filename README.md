Account is a django user registeration app that uses django-material for forms
This app handles the features like user login, user signup, reset password, forgot password.

##### Requirements 
* [django-material](https://github.com/viewflow/django-material) app, to make forms beautiful


##### Setting up
* Add 'account' and 'material'(django-material) app to your installed apps in settings file
```
INSTALLED_APPS = (
....
....
'account',
'material',
)
```
* Add template directory to the project
```
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [os.path.join(BASE_DIR, 'templates')],
....
....
}
]
```
* Define LOGIN_URL, LOGOUT_URL, LOGIN_REDIRECT_URL in settings file
```
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
```
* Email setting in settings file
```
DEFAULT_FROM_USER = '' # your email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '' # host email
EMAIL_HOST_PASSWORD = '' # your app password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```
* Using HTTPS or HTTP. If using https use the following in settings file
```
USE_HTTPS = True
```


