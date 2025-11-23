# home_assignment_qa — Automated API Testing Framework

A fully asynchronous, modern Python testing framework built for API automation using **pytest**, **httpx**, **pydantic v2**, **faker**, **custom retry mechanisms**, and **real-time Allure reports hosted on GitHub Pages**.

This project is based on the assignment for **Automation QA Engineer — Home Task**, extended with CI/CD, reporting, and best engineering practices.

---

## 🚀 Features

### ✔ Fully async API test framework  
Powered by **httpx.AsyncClient**, providing fast and reliable test execution.

### ✔ Strong schema validation  
Using **Pydantic v2** and **pydantic-settings** for configuration and response validation.

### ✔ Custom retry decorator  
Retries flaky requests with logging of each retry attempt.

### ✔ Random test data generation  
Dynamic payloads created with **Faker** and Pydantic models.

### ✔ Allure Reporting (modern)  
- Allure CLI integration  
- Automatic report generation in GitHub Actions  
- Report deployment to **GitHub Pages**

### ✔ Clean architecture  
Industry-standard folder structure (`src/`, `tests/`, `config/`).

### ✔ CI/CD pipeline  
GitHub Actions workflow that:
1. Installs dependencies  
2. Runs tests  
3. Generates Allure HTML report  
4. Deploys it to **GitHub Pages**

---

## 🌐 Live Allure Report

The latest test report is publicly available here:

👉 **https://SalamiSlasher.github.io/home_assignment_qa/**

---

## 🧩 Technology Stack

| Component         |
|-------------------|
| Python 3.13+      |
| pytest            |
| pytest-asyncio    |
| httpx             |
| pydantic v2       |
| pydantic-settings |
| faker             |
| allure-pytest     |
| GitHub Actions    |
| GitHub Pages      |

---

## 📁 Project Structure

```
home_assignment_qa/
│
├── config/
│   └── settings.py            # Configuration via pydantic-settings
│
├── src/
│   └── httpbin_framework/
│       ├── client.py          # Async httpx wrapper + retry logic
│       ├── retry.py           # Custom retry decorator
│       ├── models.py          # Pydantic response models
│       ├── logger.py          # Logging setup
│       └── data/
│           ├── generators.py  # Faker-based utilities
│
├── tests/
│   ├── test_response_formats.py
│   ├── test_request_inspection.py
│   ├── test_dynamic_data.py
│   └── conftest.py
│
├── .github/
│   └── workflows/
│       └── allure_pages.yml   # CI + Allure Pages deployment
│
├── .env                       # User configuration variables
├── README.md
├── pyproject.toml             # Dependencies & pytest config
└── pytest.ini                 # Pytest settings
```

---

## ⚙️ Configuration

Project configuration is loaded from `.env`:

Example:

```
BASE_URL=https://httpbin.org
TIMEOUT=5
RETRIES=3
RETRY_BACKOFF=0.5
```

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/SalamiSlasher/home_assignment_qa.git
cd home_assignment_qa
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scriptsctivate      # Windows
```

Install dependencies:

```bash
pip install -e .
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest -v
```

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

---

## 📊 Allure Reporting

### Local Allure CLI

If Allure CLI is installed:

```bash
allure serve allure-results
```

Generate static report:

```bash
allure generate allure-results -o allure-report --clean
```

---

## ☁️ CI/CD (GitHub Actions)

The repository includes a workflow that:

1. Installs Python  
2. Installs project dependencies  
3. Runs pytest with Allure  
4. Generates HTML Allure report  
5. Publishes Allure report to **GitHub Pages**

Workflow file:

```
.github/workflows/allure_pages.yml
```

After each push to `main`, the report updates automatically.

---
