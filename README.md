# 📊 Stock Analytics Dashboard – Backend

This is the **backend service** for the Stock Analytics Dashboard project.  
It is built with **FastAPI** and integrates with **Yahoo Finance** to fetch stock market data.  
It also supports authentication and caching for efficient API performance.

---

## 🚀 Features
- 📈 Fetch real-time and historical stock data from Yahoo Finance  
- 🔒 Authentication support  
- ⚡ Fast and lightweight API with FastAPI  
- 🗂️ Caching utilities for performance  
- 🛠️ Pydantic models and dependency injection  

---

## 🏗️ Project Structure

```bash
backend/
│── app/
│   ├── cache.py          # Cache utilities
│   ├── deps.py           # Dependencies for FastAPI
│   ├── models.py         # Pydantic models & schemas
│── auth.py               # Authentication logic
│── main.py               # FastAPI entry point
│── yfinance_client.py    # Yahoo Finance data fetcher
│── requirements.txt      # Python dependencies
│── .env.local            # Environment variables
│── .gitignore
│── LICENSE
│── README.md
```
⚙️ Setup Instructions

1️⃣ Clone the repository
```bash
git clone https://github.com/Abhinavmamidwar/stock-dashboard-backend.git
cd stock-dashboard-backend
```

2️⃣ Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Setup environment variables
Create a .env.local file in the root directory and configure:
```bash
SECRET_KEY=your_secret_key
API_KEY=your_api_key   # if required
```
5️⃣ Run the backend server
```bash
uvicorn main:app --reload
```

Backend will run at:
👉 http://127.0.0.1:8000

📌 API Documentation

Once the server is running, you can access:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📄 License

This project is licensed under the MIT License.
