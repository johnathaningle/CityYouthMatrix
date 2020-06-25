# CityYouthMatrix
Tech Frederick Hackathon Submission

This is a Python project making use of the Django framework.

## Development
To get started locally, do the following:

```
virtualenv cym
source cym/bin/activate
pip install -r requirements.txt
```

To setup the database run `python manage.py migrate`. This will initialize a local SQLite databases with the appropriate tables.

Next, open a shell into the app with `python manage.py shell` and execute the following lines (substituting the desired values) to create a superuser:

```python
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.create_superuser('First', 'Last', '555-555-5555', 'email@email.com', password='test')
```

Once that is done, you can run the server locally with `python manage.py runserver`.

## Deployment
This app is configured to deploy to Heroku but could easily be deployed elsewhere. Deployment requires the following environment variables:

* `DATABASE_URL`: A PostgreSQL database connection string
* `DJANGO_SETTINGS_MODULE`: Name of the settings module, eg `cityyouthmatrix.settings.heroku`
* `SECRET_KEY`: A random sequence to secure the app

The local development server is not appropriate for a production deploy. `gunicorn` is recommended.
