# 🧩 Automation Framework Documentation – E2E Ecommerce Website

## Overview
Developed using Python, Selenium, Pytest, and Requests for automating the [Automation Exercise](https://automationexercise.com/) site.

## Folder Structure
```
E2E_Ecommerce_Automation/
│
├── api_clients/              # API request handling
├── Page_Pom/                 # Page Object Model classes
├── Data/                     # Test data (JSON)
├── Tests/                    # Test cases (UI + API)
├── Reports/                  # Allure & HTML reports
└── Config/                   # Environment configs
```
---

## ⚙️ Tools & Technologies
- **Language:** Python  
- **Frameworks:** Pytest, Selenium, Requests  
- **Reporting:** Allure, pytest-html  
- **Design Pattern:** Page Object Model (POM)  
- **Version Control:** Git / GitHub  

---
## Execution Commands
```bash
pytest -v --html=Reports/report.html --alluredir=Reports/allure-results
allure serve Reports/allure-results
```
