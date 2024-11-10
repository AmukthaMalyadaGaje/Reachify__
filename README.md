
# **Reachify Full Stack Assignment**

## **Overview**
This repository contains the full-stack solution for the Reachify project, which includes both the **frontend** and **backend** components. The project is designed to be a fully functional application with clear setup guides for each part.

### **Components**
1. **Frontend**: Built using **React.js**, **Vite**, and **Tailwind CSS** for a responsive and modern UI.
2. **Backend**: Built with **FastAPI** and **Python**, designed to handle data processing and serve APIs efficiently.

## **Frontend**

### **Technologies Used**
- **React.js**: For building the user interface.
- **Vite**: A build tool that provides a fast development experience.
- **Tailwind CSS**: For styling the application in a scalable and efficient way.
- **Fetch**: To handle HTTP requests between frontend and backend.

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Reachify-Full-Stack-Assignment.git
   cd Reachify-Full-Stack-Assignment/FE
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   Your frontend application will be available at [http://localhost:3000](http://localhost:3000).

### **Features**
- **Interactive UI**: Allows users to interact with backend services for different functionalities.
- **API Communication**: Communicates with the backend to fetch data and display it dynamically.
- **Responsive Design**: Built to be fully responsive across different screen sizes.

## **Backend**

### **Technologies Used**
- **FastAPI**: A high-performance Python web framework for building APIs.
- **Uvicorn**: ASGI server for serving the FastAPI app.
- **Pydantic**: For data validation and parsing.
- **Docker**: Containerization to deploy the application.

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Reachify-Full-Stack-Assignment.git
   cd Reachify-Full-Stack-Assignment/BE
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be available at [http://localhost:8000](http://localhost:8000).

### **Features**
- **REST APIs**: Provides endpoints to interact with frontend components.
- **Data Processing**: Handles data processing, such as label extraction, expiry prediction, and freshness evaluation.
- **Authentication**: Includes token-based authentication for secure communication.

## **Docker Setup**

### **Frontend Docker Setup**
1. Navigate to the `FE` directory.
2. Build the frontend Docker image:
   ```bash
   docker build -t frontend .
   ```
3. Run the frontend container:
   ```bash
   docker run -p 3000:3000 frontend
   ```

### **Backend Docker Setup**
1. Navigate to the `BE` directory.
2. Build the backend Docker image:
   ```bash
   docker build -t backend .
   ```
3. Run the backend container:
   ```bash
   docker run -p 8000:8000 backend
   ```

## **GitHub Repository Structure**

```bash
Reachify-Full-Stack-Assignment/
├── BE/                 # Backend folder
│   ├── main.py         # FastAPI app entry point
│   ├── requirements.txt# Backend dependencies
│   ├── Dockerfile      # Dockerfile for backend
│   └── ...             # Additional backend code
├── FE/                 # Frontend folder
│   ├── package.json    # Frontend dependencies
│   ├── src/            # React components and assets
│   ├── Dockerfile      # Dockerfile for frontend
│   └── ...             # Additional frontend code
└── README.md           # This README file
```
