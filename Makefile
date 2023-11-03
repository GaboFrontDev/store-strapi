pull:
	git pull
build:
	docker-compose build telludire_deployer_backend

tag:
	docker tag image-backend-strapi-telludire_deployer_backend docker.telluridedigitalworks.com:444/telludire_deployer_backend:latest

push:
	docker push docker.telluridedigitalworks.com:444/ribcity-template:latest
