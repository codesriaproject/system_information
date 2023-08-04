Django sign up testing package
==============================

**Description:**

    The main motive is to upload our own package on PyPI. so for doing testing, I have
    uploaded it on this platform.

**installation:**

Just run a command on the terminal 

    pip install Django_sign_up.


1. 	Add into an installed app of settings.py file

		INSTALLED_APPS = [
		...
		'Django_sign_up',
		...
		]

2. 	Then add this URL in the main urls.py  

		url(r'', include('Django_sign_up.url')),


3. 	Include this template tag in the template file where you want to display the form :

		{% include 'Django_sign_up/register.html' %}

