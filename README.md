# Instructions

1. Build pull etc docker images
2. Do `make bash` to:
    1. `createuser` and `createdb`
    2. `kbblog/manage.py migrate`
    3. `kbblog/manage.py createsuperuser`
3. Do `make up`
4. Go to `localhost:8010/admin` and make some stuff
5. Go to `localhost:8010/articles`to start exploring the API
