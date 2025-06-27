# 🛠️ Asset Reminder API

This is a Django REST API project to help you manage assets with important dates like service and expiration.  
It reminds you **before** something is due and records if something is **missed**.

---

## 🔍 What This Project Does

Every asset you add has two important times:
- **Service Time** – When maintenance is due
- **Expiration Time** – When the asset is no longer valid

This API does 3 things:
1. Sends a reminder 15 minutes before service or expiration
2. Logs a **Notification** in the system
3. If the time is missed, logs a **Violation** for that asset

---

## 🔧 Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite (default DB)
- Git & GitHub

---

## 🚀 How to Run This Project

1. Clone this repository:
   ```bash
   git clone https://github.com/rchtchauhan/asset-reminder-api.git
   cd asset-reminder-api

