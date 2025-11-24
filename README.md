# Personal Finance Advisor  
*Build a personal finance advisor based on spending patterns.*

![Project Banner](assets/banner.png)

## 📌 Overview
This project is a Python-based personal finance advisor that analyzes real spending patterns and generates data-driven recommendations.  
Instead of generic budgeting tips, the system processes actual transaction records, identifies patterns, detects anomalies, and provides tailored financial insights.

The goal is simple: **help users understand where their money goes and how to use it better.**

---

## ⚙️ Features
### ✅ Core Functionality
- **Transaction Import:** Load CSV/OFX files with bank transactions.  
- **Merchant Normalization:** Clean and standardize merchant names.  
- **Expense Categorization:** Rule-based categorizer with ML-ready hooks.  
- **Spending Pattern Analysis:** Monthly aggregation + clustering to reveal trends.  
- **Recurring Payment Detection:** Identify subscriptions and repeated charges.  
- **Anomaly Detection:** Flag suspicious or unusually large expenses.  
- **Personalized Recommendations:** Budget targets, saving opportunities, overspending alerts.

### 🧩 Architecture
Modular Python codebase:
- `ingest.py` – transaction loading  
- `preprocess.py` – cleaning + categorization  
- `feature_engineering.py` – monthly feature creation  
- `analytics.py` – clustering and pattern discovery  
- `recommender.py` – generates actionable advice  
- `prototype_main.py` – end-to-end execution pipeline  

---

## 🔧 Tech Stack
- **Python 3.10+**  
- **pandas** — data processing  
- **scikit-learn** — clustering & analytics  
- **rapidfuzz** — merchant normalization  
- **matplotlib** — future dashboards and reports  
- *(Optional)* Flask/FastAPI for API  
- *(Optional)* SQLite/PostgreSQL for persistent storage  

---

## 📂 Project Structure
