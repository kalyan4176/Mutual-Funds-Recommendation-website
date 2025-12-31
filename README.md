# Mutual Fund Recommendation System

A full-stack web application that provides personalized mutual fund recommendations based on user financial profiles using Machine Learning. It also includes educational content and financial calculators (SIP, SWP, Real Returns) to assist investors.

## Features

-   **Personalized Recommendations**: Uses a K-Nearest Neighbors (KNN) algorithm to match user profiles (age, income, risk tolerance, etc.) with suitable mutual funds.
-   **Educational Hub**: A dedicated Home page explaining Mutual Funds, their advantages, and comparisons with traditional investments.
-   **Financial Calculators**:
    -   **SIP Calculator**: Estimate returns on Systematic Investment Plans.
    -   **SWP Calculator**: Plan withdrawals with Systematic Withdrawal Plans.
    -   **Real Returns Calculator**: Calculate inflation-adjusted returns to understand true purchasing power.
-   **Responsive Design**: Fully responsive UI with a mobile-friendly navigation drawer.

## Tech Stack

### Frontend
-   **React.js**: Component-based UI library.
-   **Tailwind CSS**: Utility-first CSS framework for styling and responsiveness.
-   **Vite**: Fast build tool and development server.
-   **Axios**: For making HTTP requests to the backend.

### Backend
-   **FastAPI**: High-performance web framework for building APIs with Python.
-   **Scikit-learn**: For implementing the KNN recommendation algorithm.
-   **Pandas**: For data manipulation and analysis.
-   **Uvicorn**: ASGI server for running the FastAPI application.


## Installation & Setup

### Prerequisites
-   Node.js and npm installed.
-   Python 3.8+ installed.

### 1. Backend Setup

Navigate to the backend directory:
```bash
cd backend
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```
*Note: If `requirements.txt` is missing, install dependencies manually:*
```bash
pip install fastapi uvicorn pandas scikit-learn
```

Run the backend server:
```bash
uvicorn main:app --reload
```
The backend API will start at `http://localhost:8000`.

### 2. Frontend Setup

Open a new terminal and navigate to the frontend directory:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Run the development server:
```bash
npm run dev
```
The frontend application will start at `http://localhost:5173` (or the port shown in your terminal).

## Usage

1.  **Home Page**: Read about mutual funds and why investing is important.
2.  **Find Recommendation**: Click "Find suitable Mutual funds", fill out the questionnaire, and get personalized fund suggestions.
3.  **Calculators**: Use the SIP, SWP, and Real Returns calculators from the navigation menu to plan your investments.

## Contributing

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License

This is just a project and not for any commercial use.  