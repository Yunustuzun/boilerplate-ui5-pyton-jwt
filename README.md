#   Python Flask & OpenUI5 JWT Authentication template
This is an OpenUI5 & Python Flask template app that demonstrates the basic usage of JWT Based Authentication  with Python Flask & OpenUI5 

## Requirments
- Python 3
- Node.js 12

## Installation
### Client
- `npm install --global @ui5/cli` to install UI5 CLI
- `npm install` to install local packages
- `ui5 serve` or `npm run test` to run a local version of your app.

### Server
- `pip install -r requirements.txt` to install Python packages
- Local or remote SQL server 
- User DB table should exists.
- Appropriate local enivorment variables( .env )  
- `python run.py` to run server. 

> Note: Strongly suggested to use Virtual environment library [venv](https://docs.python.org/3/library/venv.html) for real projects. It runs the project in an isolated place and eliminates package dependencies.


## Step-by-step process
- The client sends the username and password to the server,
- Server verifies the credentials; if it retrieves the user data, generates a JWT containing user details and permissions that will be used to access the services, 
- It also sets the expiration on the JWT.
- Then the server takes a secret key and uses it to sign it to the client as a response to the request.
- Client sends the stored JWT in an Authorization header for every request to the server
### Files that manage the most of process 
-   `server/api/auth.py`
-   `client/webapp/class/User.js`  
-   `client/webapp/class/Backend.js` 
