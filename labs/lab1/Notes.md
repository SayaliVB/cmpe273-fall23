
Commands used:

1. Install fast api and uvicorn:
=> pip3 install fastapi
=> pip3 install uvicorn

2. uvicorn was not added to path variables, hence added python3 -m to reload command
=> python3 -m uvicorn main:app --reload

3. OpenAPI spec
=> http://127.0.0.1:8000/docs
=> http://127.0.0.1:8000/redoc

4. Generate python client from OpenAPI Spec
=> pip3 install openapi-python-client


**Use _ instead of -**
=> python3 -m openapi_python_client generate --url https://my.api.com/openapi.json
**Update OpenAPI version in main.py() since error in generating client for the default version**
