# backend-project-architecture

A modular Python backend architecture built with Flask, inspired by Clean Architecture principles. Designed for scalable, testable, and maintainable applications.

---

### Project Structure

* `configs/` – Environment and config files
* `src/`
  * `app/` – Flask app setup and routing
    * `blueprints/` – Flask Blueprints
    * `controllers/` – HTTP request controllers
    * `interfaces/` – REST or other API interfaces
    * `presenters/` – Response formatting and output
    * `create_flask_app.py` – Flask app factory
  * `infa/` – Infrastructure layer
    * `db/` – Database interactions
    * `interactor/` – Core application logic
    * `dtos/` – Data Transfer Objects
    * `errors/` – Error handling
    * `interfaces/` – Abstract interfaces
    * `use_cases/` – Business use cases
    * `validations/` – Input validation
  * `test/` – Unit and integration tests
* `conftest.py` – Test configuration


###### Principles

- Clear separation of concerns (presentation / domain / infrastructure)
- Lightweight dependencies
- DTO-based communication
- Easy to test
- Environment-aware config loading
