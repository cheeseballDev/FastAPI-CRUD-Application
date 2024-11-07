# A simple CRUD application using FastAPI

## PREREQUISITES: 
- Python3
- MongoDB
- Insomnia (or any API platform)

## STEPS HOW TO RUN THE APPLICATION (using VSCode):
1. Using any terminal, go to the directory where all of your files in in
2. Create a virtual environment inside the directory by entering the command: ```python -m nenv env```
3. Activate the virtual environment depending on your Operating System.
4. Install the following dependencies: ```pip install fastapi uvicorn beanie``` 
5. Create a .env file in the directory
6. Add ```MONGODB = <your mongodb address>``` inside the .env file and save it (make sure MongoDB is already running)
7. Run the program by entering the command ```python run.py```

## STEPS HOW TO TEST THE APPLICATION (using an API platform):
### FOR POST:
1. Create a POST HTTP request and enter in the following endpoint ```localhost:3000/api/user```
2. Add a JSON body like shown below:
```
{
	"name":"Example name",
	"email":"examplename@example.com"
}
```
3. Send the request

### FOR GET (one user):
1. Create a GET HTTP request and enter in the following endpoint ```localhost:3000/api/user/<id>```
2. Send the request
* *NOTE: You need to create a user beforehand to be able to retrieve the user* *
### FOR GET (all users):
1. Create a GET HTTP request and enter in the following endpoint ```localhost:3000/api/users```
2. Send the request

### FOR UPDATE:
1. Create a PATCH HTTP request and enter in the following endpoint ```localhost:3000/api/user/<id>```
2. Add a JSON body like shown below:
```
{
	"name":"Example name 2",
}
```
3. Send the request
* *NOTE: You need to create a user beforehand to be able to update an existing user* *

### FOR DELETE:
1. Create a DELETE HTTP request and enter in the following endpoint ```localhost:3000/api/user/<ANY EXISTING ID>```
2. Send the request
3. * *NOTE: You need to create a user beforehand to be able to delete a user* *

