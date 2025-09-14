# ControlUP – Automation Home Test (PyTest + Selenium + Requests)

A clean, production-ready implementation of the assignment using **Python 3.10+**, **pytest**, **selenium**, and **requests**.

## What’s included
- ✅ Page Object Model for SauceDemo UI
- ✅ Robust fixtures with explicit waits & headless mode by default
- ✅ 2 UI tests (inventory count, add-to-cart badge)
- ✅ 3 API tests for Airport Gap (count, contains airports, distance > 400km)
- ✅ Lightweight configuration via environment variables / `.env`

---

## Quick Start

1) **Create & activate a virtualenv (recommended):**
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
```

2) **Install dependencies:**
```bash
pip install -r requirements.txt
```

3) **(Optional) Copy and adjust environment vars:**
```bash
cp .env.example .env
# edit values if desired
```

4) **Run all tests (headless by default):**
```bash
pytest -q
```

## Notes on Implementation
- **Selenium Manager** (bundled with Selenium 4.2+) auto-resolves the driver; no extra setup required.
- Explicit waits via `WebDriverWait` for stable UI operations.
- Assertions are **tight but resilient** (correct selectors, trimmed text comparisons).
- API tests use `requests` and validate **status codes**, **schemas**, and **values**.
- Clean code & readability prioritized (type hints, docstrings, POM).

---
