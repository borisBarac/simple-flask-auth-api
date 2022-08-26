
### Run mongo container
> docker run --name mongo -d -p 27017:27017

### Run Flask
> pip3 install -r requirements.txt
> flask --app ./api/app --debug run