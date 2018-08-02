# Installation

## 1. Pull this repo

```bash
git clone git clone https://github.com/kbairak/jsonapi_demo.git
cd jsonapi_demo
```

## 2. Build, pull and start the containers

```bash
make build up
```

## 3. Create database role, database, migrate and create a superuser

```bash
make bash
  createuser -h db -U postgres kbairak
  createdb -h db -U postgres -O kbairak kbblog
  kbblog/manage.py migrate
  kbblog/manage.py createsuperuser
  exit
```

# Endpoints

The `/admin` URL houses the Django admin panel. You can create users and
articles from there if you want.

The API is mounted on `/articles`. You can visit it with your browser as well.
The following operations are supported:

- `GET /articles` => Get a list of all articles, no pagination/filtering implemented yet
- `POST /articles` => Create a new article
- `GET /articles/:article_id` => Get a specific article

The format of the request and response payloads follows the {JSON:api}
specification.

# Code

The views are deliberately kept very simple. The bulk of the representation and
validation work is done from the serializers. However, the serializers are
**only** responsible for:
- converting database entities into JSON representations
- validating JSON payloads and
- converting JSON payloads to a collection of validated data

# TODOs:

1. On validation errors, django-rest-framework's default error formatting is
   used. We should implement {JSON:api}'s formatting.
2. Pagination
3. Filters
