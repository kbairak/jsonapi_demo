build:
	docker-compose build

bash:
	docker-compose run --rm web bash

up:
	docker-compose up -d

down:
	docker-compose stop web
	docker-compose rm -f web

restart:
	docker-compose restart web

logs:
	docker-compose logs -f --tail=40 web

shell_plain:
	docker-compose run --rm web kbblog/manage.py shell

shell_plus:
	docker-compose run --rm web kbblog/manage.py shell_plus

shell: shell_plus

runserver: down
	docker-compose run --rm --service-ports web
