# 🚀 Python Environment Setup Guide

## Quick Start

### 1. **Install Dependencies**

```powershell
# Activate your virtual environment
.\Scripts\activate

# Install all required packages
pip install -r requirements.txt
```

### 2. **Configure Environment Variables**

```powershell
# Copy the template
copy .env.example .env

# Edit .env with your actual credentials
notepad .env
```

**⚠️ IMPORTANT:** Never commit `.env` to version control!

### 3. **Verify Setup**

```python
# Test environment loading
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print('Oracle User:', os.getenv('ORACLE_USER'))"
```

---

## 📁 File Overview

| File | Purpose | Commit to Git? |
|------|---------|----------------|
| `requirements.txt` | Package dependencies | ✅ Yes |
| `.env.example` | Template for environment variables | ✅ Yes |
| `.env` | **Your actual credentials** | ❌ **NEVER** |
| `.gitignore` | Files to ignore in Git | ✅ Yes |

---

## 🔒 Security Best Practices

### DO:
- ✅ Use `.env` for all credentials
- ✅ Keep `.env` in `.gitignore`
- ✅ Use `.env.example` as a template
- ✅ Rotate credentials regularly
- ✅ Use environment-specific `.env` files (`.env.dev`, `.env.prod`)

### DON'T:
- ❌ Hardcode passwords in Python files
- ❌ Commit `.env` to Git
- ❌ Share `.env` via email/chat
- ❌ Use production credentials in development

---

## 📦 Installing Dependencies

### Full Installation
```powershell
pip install -r requirements.txt
```

### Install Only Core Packages
```powershell
pip install pandas numpy requests beautifulsoup4 selenium python-dotenv
```

### Install for Development
```powershell
pip install -r requirements.txt
pip install pytest pytest-cov flake8 black mypy
```

---

## 🔧 Migrating Existing Scripts

### Before (Hardcoded Credentials)
```python
# ❌ BAD - Remove this from your scripts
un = 'reporting_read'
pw = 'UzKmKZaLTh9sJIbBHXqzmjwI'
cs = 'vxtmobproddb02.genco.com:1561/STARPRD'
```

### After (Using Environment Variables)
```python
# ✅ GOOD - Use this pattern
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

ORACLE_USER = os.getenv('ORACLE_USER')
ORACLE_PASSWORD = os.getenv('ORACLE_PASSWORD')
ORACLE_CONN = os.getenv('ORACLE_CONN_STRING')

# Use in connection
connection = pyodbc.connect(
    f"DRIVER={{Oracle}};UID={ORACLE_USER};PWD={ORACLE_PASSWORD};DSN={ORACLE_CONN}"
)
```

---

## 📝 Updating Your Scripts

### Scripts That Need Credential Updates:
- [ ] `Oracle sql.py`
- [ ] `Slnm_NVQry_WeeklyExports.py`
- [ ] `py ssrs.py`
- [ ] `UKGtoSQL.py`
- [ ] `email.py`
- [ ] All `Oracle_*.py` files
- [ ] All `Slnm_NVQry_*.py` files

### Template for Database Connections

#### Oracle
```python
import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def get_oracle_connection():
    return oracledb.connect(
        user=os.getenv('ORACLE_USER'),
        password=os.getenv('ORACLE_PASSWORD'),
        dsn=os.getenv('ORACLE_CONN_STRING')
    )
```

#### SQL Server
```python
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_sql_connection():
    conn_str = os.getenv('SQL_SERVER_CONN_STRING')
    return pyodbc.connect(conn_str)
```

---

## 🧪 Testing Your Setup

```python
# test_env.py
from dotenv import load_dotenv
import os

load_dotenv()

print("✅ Environment loaded successfully!")
print(f"Oracle User: {os.getenv('ORACLE_USER')}")
print(f"Environment: {os.getenv('ENV')}")
print(f"Debug Mode: {os.getenv('DEBUG')}")
```

Run: `python test_env.py`

---

## 📚 Next Steps

1. ✅ **Update credentials** in `.env` with your actual values
2. ✅ **Install dependencies**: `pip install -r requirements.txt`
3. ✅ **Test environment loading**: Run the test script above
4. ✅ **Update existing scripts** to use environment variables
5. ✅ **Remove hardcoded credentials** from all Python files
6. ✅ **Create utility modules** (see improvement plan)

---

## 🆘 Troubleshooting

### "Module not found" after installation
```powershell
# Make sure venv is activated
.\Scripts\activate
pip install -r requirements.txt
```

### ".env not loading"
```python
# Check .env file location
import os
print(os.path.exists('.env'))  # Should be True

# Use absolute path if needed
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)
```

### "Credential still showing as hardcoded"
- Search for hardcoded values: `grep -r "password=" *.py`
- Replace with `os.getenv()` calls
- Test thoroughly before deleting old code

---

## 📞 Need Help?

- Python-dotenv docs: https://pypi.org/project/python-dotenv/
- Environment variables best practices: https://12factor.net/config
