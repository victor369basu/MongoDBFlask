# MongoDBFastAPI
This repository explains how to create a REST API using Python and host it locally using Docker. The goal of this task is to allow the user to interact with a database of products using APIs which are available on localhost via Docker.<br>
At first, E-commerce products and its information data have been hosted on a MongoDB server. Connecting to the MongoDB server and operating basic crud operation is explained in the "MongoAPI.py" file. <br>
REST API has been created with the help of FastAPI, that allows the user to do basic CRUD operations on the data. This process is explained in "__init__.py" file.<br>
After that Dockerization of API is performed by the following command below.<br>
``` python
docker pull mongo
```
``` python
docker create -it --name MongoTest -p 5000:27017 mongo
```
``` Python
docker start MongoTest
```
``` Python
docker compose build myreader
```
``` Python
docker compose run -p 5001:5001 myreader
```
## CRUD operations

Lets operate some basic CRUD operations over the REST API.
<br>
![base](images/victor_base.png?raw=true)
<br>
### Read
![read](images/victor_read.png?raw=true)
<br>
### Write
![write](images/victor_write.png?raw=true)
![write_mongo](images/victor_write_mongodb.png?raw=true)
<br>
### Update
![update](images/victor_update.png?raw=true)
![update_mongo](images/victor_update_mongodb.png?raw=true)
<br>
### Delete
![delete](images/victor_delete.png?raw=true)
![delete_mongo](images/victor_delete_mongodb.png?raw=true)
