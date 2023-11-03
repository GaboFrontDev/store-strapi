pull:
	git pull
build:
	docker-compose build telludire_deployer_backend

tag:
	docker tag image-backend-strapi_telludire_deployer_backend docker.telluridedigitalworks.com:444/telludire_deployer_backend:latest

push:
	docker push https://docker.telluridedigitalworks.com:444/telludire_deployer_backend:latest
