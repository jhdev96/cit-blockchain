# cit-blockchain
A blockchain app for tracking and updating student records. 
When a new student is added to the citinstitute database,
or an existing student's info is updated, a new block with a
unique hash is added to the network.

### Running this app
Running this app requires Docker. If you don't have Docker
installed, go here: https://www.docker.com/products/docker-desktop

### Set up for Dev Environment
- docker-compose -f docker-compose.dev.yml up --build
- To create an admin account run:
   ```docker-compose exec web python manage.py createsuperuser```


### Set up for Prod Environment
- docker-compose up --build
