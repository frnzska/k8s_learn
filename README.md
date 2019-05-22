### Docker

Test dockerfile:
 
`docker build -t flask8s:latest .`

`docker run -d -p 5000:5000 flask8s`

with docker compose:

`docker-compose up`

`docker-compose down`

other:

`docker ps` (show containers)

`docker stop <container_id>`

`docker inspect <container_id`>

`docker inspect <container_name`>

get size of image:

`docker inspect  k8s_learn_worker:latest --format='{{.Size}}'
`

connection in web container to db:
postgres://db:5432

from host:
postgres://0.0.0.0:5432

### Kubernetes
