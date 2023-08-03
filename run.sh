FILE=docker-compose.flask.yml
docker-compose -f $FILE down --remove-orphans
docker-compose -f $FILE build
docker-compose -f $FILE up