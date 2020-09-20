# myBlog
This a blog application with multi features. User Authentication with email, and CRUD functionalities. User Profile. In  Back-end used  Django and front-end are HTML, CSS ,  a little JS.


download or clone the repository.
Enable virtual environment.
install dependecies from requirements.txt

update settings.py(email) with your account info.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your gmail account'(put your gmail)
EMAIL_HOST_PASSWORD = "your gmail account password"(put your password)
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@myblog.com'

then enable less sucure app from your gmail account settings.
