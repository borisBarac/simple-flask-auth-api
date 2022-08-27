# Simple Flask Auth API

- Simple and extendable Api with AUTH support
- Intended for usage with **example** FE projects where i want to be able to authenticate the user

## Development Run

### Run mongo container
> docker run --name mongo -d -p 27017:27017

### Run Flask
> pip3 install -r requirements.txt
> flask --app ./api/app --debug run

## Release Run
> docker-compose up