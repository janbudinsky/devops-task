# Simple Metrics
Implement declared endpoints for metrics retrieval and deploy the application in docker on given server.

### Application
Implement endpoints for basic metrics retrieval from the server where the application is running.
Endpoints to be implemented are declared in `metrics/main.py`, each returning metrics for respective resources:
* CPU
* RAM
* disk
* network (traffic)
* list of services running on the server

Each endpoint should return data as `JSON`, it's up to you what structure will data have and which data are relevant for each endpoint.
If the code for the endpoints implementation will be more complex than few lines, move the logic to separate file(s) and import it from there.

#### Requirements
Python version: `3.6+`

Required python packages are stored in `requirements.txt` using `pip` format, feel free to add some if necessary.

### Deployment
The server on which the application will be deployed has plain ubuntu installed, so install what is necessary.
Write a `Dockerfile` for the application (it can be started using `python metrics/main.py` command), deploy the application in docker.
Allow access to the server only for IP addresses given in the email (and any other you need yourself).
Once deployed, you can check 2 already implemented dummy endpoints to verify the application is working - `/` and `/hello/<name>`.
