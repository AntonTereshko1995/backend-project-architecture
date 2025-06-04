
# 🔐 Key-Value Store API

A simple REST API for storing and managing key-value pairs using Flask and Redis.
Author: **Anton Tereshko**

---

### 📦 API Endpoints

###### 1. Create a Key
curl -X POST -H "Content-Type: application/json"
-d '{"key": "test_key", "value": "test_value"}'
http://localhost:5000/v1/create/

###### 1. Delete a Key
curl -X DELETE http://localhost:5000/v1/delete/[KEY]

###### 2. Update a Key
curl -X PUT -H "Content-Type: application/json"
-d '{"key": "test_key", "value": "new_value"}'
http://localhost:5000/v1/update/

###### 3. Get a Key
curl -X GET http://localhost:5000/v1/get/[KEY]

---

### 🚀 Start the Project

Main entry file:
python flask_process_handler.py

---

### 🔧 Planned Improvements

###### 1. Implement Automated Test Cases

* Add **unit and integration tests** for all API endpoints and repository logic.
* Use frameworks like `pytest` or `unittest` to ensure correctness and stability.
* Include test coverage reports to track and improve test completeness.
* Enable CI (e.g., GitHub Actions) to automatically run tests on each commit.

###### 2. Add Docker Support

* Create a `Dockerfile` to package the Flask app and its dependencies.
* Create a `docker-compose.yml` file to run the app alongside Redis.
* Benefit: consistent development and production environments, easy deployment.

###### 3. Configure Redis Environment

* Improve Redis connection handling for local host).

###### 4. Add More Logging

* Add structured and informative logging using the `logging` module.
* Log events like:
  * API calls and request data
  * Cache hits and misses
  * Key creation, update, and deletion
  * Exceptions and system errors
* Optionally support log levels (`INFO`, `WARNING`, `ERROR`, `DEBUG`) and log files.

###### 4. Settings file

* Add a file to load all libraries within the project automatically.
