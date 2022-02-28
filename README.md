# aifora-task
## Local Setup

1. `pip install poetry`
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. Run the FastAPI server via poetry `poetry run ./run.sh`
4. Open http://localhost:8001/docs
5. Click the 'PUT' button
6. Click the 'Click the try it out' button
7. In the 'groupKey' text field enter 'option1'
8. In the 'Request body' text box enter the json contained in the curl_request.json file contained in this repo.
9. The required request will be returned in the 'Response Body' window.
