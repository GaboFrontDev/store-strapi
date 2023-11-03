pull:
	git pull
build:
	docker-compose build telludire_deployer_backend

tag:
	docker tag image-backend-strapi_telludire_deployer_backend docker.telluridedigitalworks.com/telludire_deployer_backend:latest

push:
	docker push docker.telluridedigitalworks.com/telludire_deployer_backend:latest
