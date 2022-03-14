# Aifora take-home task

Write a Python Rest-Service which takes input requests of the form "test\_request.json". (Part of the files in this repository.)

And yields responses of the form "test\_response.json". (Part of the files in this repository.)

Provide a suitable way to start the service locally.

The task is succesfully completed if the provided curl_request.txt (Part of the files in this repository.) - yields a valid response. The actual optimization logic is not important
for this task and all short cuts are allowed.

## Local Setup

1. `pip install poetry`
2. Install dependencies: `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. Run the FastAPI server via poetry `poetry run ./run.sh`
4. Open <http://localhost:8001/docs>
5. Click the 'POST' buttons to send POST requests to the API
6. Click the 'GET' buttons to send GET requests to the API
7. Use the supplied test\_response.json and test\_reply.json as request body inputs to the requests
8. It is noted that curl\_request.txt returned a valid response when tested
=======
## Local Setup

1. `pip install poetry`
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. Run the FastAPI server via poetry `poetry run ./run.sh`
4. Open <http://localhost:8001/docs>
5. Click the 'PUT' button
6. Click the 'Click the try it out' button
7. In the 'groupKey' text field enter 'option1'
8. In the 'Request body' text box enter the json contained in the curl\_request.json file contained in this repo.
9. The required request will be returned in the 'Response Body' window.
