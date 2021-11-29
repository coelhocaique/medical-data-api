# Medical Data API

## Technologies Used

* [Python 3](https://www.python.org/)
* [SqlAlchemy](https://www.sqlalchemy.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Uvicorn](https://www.uvicorn.org/)

## Run App

Run locally with Python:

```
 python3 src/main.py

```
Or run with [docker](https://docs.docker.com/get-docker/):
```
cd docker
docker-compose up
```

Note: Replace the ```<IP_ADRESS>``` under ```docker-compose.yml``` with your ip address, it is needed in order to the database 
connect properly with the application.

To populate the data hit ```python3 src/populate_db.py``` after application is up!

## How to use the API

After application is started you can access [Swagger Documentation](http://localhost:8000/docs)

Note: It was not possible to process all the dataset to create the postgresql image, so I would need more time to process all the data, but there is a good amount of data in the database

## About the solution

After analyzing the data, I found out that it would be a good use case to have APIs to query average costs data by ***HCPCS Code***, so I basically created 
some basic statistics using this field.

So, the APIs variations that I created are:

* Query by ***HCPCS Code***
* Query by ***HCPCS Code*** and ***Country***
* Query by ***HCPCS Code*** and ***City*** 
* Query by ***HCPCS Code*** and ***State*** 

I think it would be useful for a provider to query these values and take it as a reference to take decisions.
 
##### DB Model
  
  I basically created only one table to store the processed data.

* ***provider_service_stats***:
    ``` 
    id = id of the table
    hcpcs_code = hcpcs code
    hcpcs_description = hcpcs code
    stats_key = used to improve and make the query faster, it is basically the variations I created under hcpcs_code
    total_services = the total number of services
    avg_submitted_charged = the sum of all avg submiited amount
    avg_medicare_pay_amount = the sum of all medicare pay amount
    avg_medicare_allowed_amount = the sum of all medicare allowed amount 
    ```


### What can be improved?

I created a scratch app the fitted in the 3, 4 hour the assignment asks to spend, so a lot of things can be improved, for example:

Create unit tests

Analyze better the data to check if the statistics provided by the api makes sense

Create more APIs with more statistics



