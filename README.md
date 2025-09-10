📊 Stock Analytics Dashboard – Backend

This repository contains the backend service for the Stock Analytics Dashboard. It provides REST APIs to fetch, process, and serve stock market data using FastAPI and integrates with Yahoo Finance (yfinance) for real-time data.

🚀 Features

🔑 Authentication system (auth.py)

📈 Stock data fetching via yfinance_client.py

⚡ FastAPI framework for building APIs (main.py)

🛠️ Dependency management (deps.py)

🗄️ Data caching for performance (app/cache.py)

📑 Models and schemas for structured responses (app/models.py)

🏗️ Project Structure
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

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/your-username/stock-dashboard-backend.git
cd stock-dashboard-backend

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env.local file in the root directory:

SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


(Add any other keys required for your authentication or APIs.)

5️⃣ Run the backend server
uvicorn main:app --reload


The API will be available at:
👉 http://127.0.0.1:8000

📌 API Endpoints
Method	Endpoint	Description
GET	/	Health check
POST	/auth/login	User login (JWT-based)
GET	/stocks/{ticker}	Fetch stock data from Yahoo
GET	/cache/status	Cache info

(Extend this table with your actual endpoints.)

🧪 Running Tests
pytest

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
