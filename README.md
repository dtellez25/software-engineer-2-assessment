# Introduction
This is a take-home assessment for a software engineer (L2) candidate. It is intended as an opportunity to demonstrate a candidate's programming and design skills.

Create a fork of this repository under your account. When you are finished, invite `reeleese` and `burtus-aurelius` as collaborators.

### The Development Environment
Provided for you are devcontainer configuration files. It is recommended that you use the devcontainer for maximum compatibility. To get started with devcontainers in VSCode, check out [Microsoft's guide](https://code.visualstudio.com/docs/devcontainers/containers).

That said, it is not a requirement to use a devcontainer. One of the reasons that this is a take home assessment is to allow you to use your own tools.


### How to run the frontend server
1. Navigate to the `frontend-server` directory.
2. Run the command `npm install` to install the required dependencies.
3. Run the command `npm start` to start the web server
4. Navigate to `localhost:3000` in your web browser. (Note: if you cannot see the webpage here, and you are running windows, you need to add an entry to your hosts file to map 127.0.0.1 to localhost)

# Software Requirements

### Python API Server
You will create an API server using python. You may import any packages you desire from pip and you may use any data storage method you desire. The requirements for the API server are as follows:

1. Create a folder called "api-server" that contains a python webserver running at 127.0.0.1:8000. You will need to implement the following actions/endpoints.
```
GET    127.0.0.1:8000/messages                // Return a list of all messages
POST   127.0.0.1:8000/messages                // Create a new message
DELETE 127.0.0.1:8000/messages/:message_id    // Delete an existing message
PUT    127.0.0.1:8000/messages/:message_id    // Update an existing message
```

2. Include a local database solution such as sqlite3 to store messages. You may use any libraries you like such as django, fastapi, etc.

3. Provide a requirements.txt file. Using a virtual environment during development is highly recommended.

4. Provide instructions for how to start the api server.


### Frontend Server
The frontend server render and styling is provided for you. You will need to handle api server queries and state management.

1. You will implement message creation, order modification, and deletion. Stubs have been left in App.tsx for you.

2. The state of messages is synced with the database such that updates to the messages are preserved after page refreshes.

3. If you really really want to style the frontend, you may. But it is not a requirement by any means.


# Documentation Requirements
1. Please comment your code.


# Running the Application

To run the full application, you will need two servers running separately: the frontend server and the backend API server.

---

## How to run the frontend server

1. Navigate to the `frontend-server` directory.
2. Run the command `npm install` to install the required dependencies.
3. Run the command `npm start` to start the web server.
4. Navigate to `localhost:3000` in your web browser. (Note: if you cannot see the webpage here, and you are running Windows, you need to add an entry to your hosts file to map 127.0.0.1 to localhost.)

---

## How to run the API server

1. Navigate to the `api-server` directory.
2. Create a Python virtual environment by running the command `python3 -m venv venv`.
3. Activate the virtual environment by running the command `source venv/bin/activate`.
4. Install the required Python dependencies by running the command `pip install -r requirements.txt`.
5. Start the API server by running the command `python pythonWebserver.py`.
6. Navigate to `127.0.0.1:8000/docs` in your web browser to view and test the API endpoints.

---

## Notes

- The frontend and backend must be running at the same time in separate terminals.
- A local SQLite3 database (`messages.db`) is used to store and persist messages.
- The database and table are created automatically when the API server first runs.
- CORS is enabled to allow smooth communication between the frontend and backend.
- The following instructions assume you are running the project inside the provided devcontainer (Linux environment). If you are using a different setup (e.g., Windows without WSL, local machine), some commands may need slight adjustments.

---

