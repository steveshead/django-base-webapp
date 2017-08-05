

# S2Design

S2Design is a Bootstrap 3 website with built in user account and user profiles. It is built with [Python][0] using the [Django Web Framework][1], and is based on Django Edge v2 by Arun Ravindran.

This project has the following basic apps:

* accounts: User account app with sign up, password reset and more.
* profiles: User profile app for authenticated users.
* contact: Contact and subscribe forms.

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv s2design`
    2. `$ . s2design/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://django-edge.readthedocs.io/en/latest/
