## Development Task for Fluvi

Backend, Python + FastAPI 

**Objective:** Create a simple FastAPI CRUD application that can create, read, update, and delete user.

### Instructions:

1. **Setup**:
   - Initialize a new Python project.
   - Install FastAPI and any other required libraries.

2. **API Endpoints**:
   - Design endpoints to create a user, get a user, update a user, and delete a user
    => POST (create user)
    => GET (get user)
    => PUT (update user) (REPLACE WITH PATCH SINCE YOU'RE NOT REPLACING THE USER)
    => DELETE (delete user)

   - The user data should have following attributes:
      - id (use UUID 4 strings)
      - name
      - email
      - created_at (datetime)

   - The data should be persistable and/or retrievable to and from MongoDB.
   - Use **Beanie** for interacting with MongoDB database. It's a hard requirement.

   - Use localhost:3000
   - No auth required for the endpoint/API
   - No encryption, no https... Keep it simple

3. **Response**:
   - The endpoints should return a JSON response for all the endpoints



5. **Additional (Optional, not required, but nice to have)**:
   - You could use Docker to containerize the application.

6. **Submission**:
   - Push your code to a public GitHub repository.
   - Include a `README.md` with clear instructions on how to run the application, test it, and any other relevant information.

### Evaluation Criteria:

1. **Functionality**: Does the application work as described?
2. **Code Quality**: Is the code organized, clean, and free of bugs?
3. **API Design**: Is the API intuitive and easy to understand?
5. **Documentation**: Are the setup and usage instructions clear?

### Documentation:
- FastAPI documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Beanie documentation: [https://beanie-odm.dev/](https://beanie-odm.dev/)