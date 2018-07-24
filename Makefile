build:
	docker-compose build

bash:
	docker-compose run --rm --service-ports web bash

up:
	docker-compose up -d

down:
	docker-compose stop web
	docker-compose rm -f web

restart:
	docker-compose restart web

logs:
	docker-compose logs -f

shell:
	docker-compose run --rm web kbblog/manage.py shell
