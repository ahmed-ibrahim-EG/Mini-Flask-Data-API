# Mini Data API

A lightweight REST API built with **Flask** to practice the fundamentals of building web APIs and handling HTTP requests and responses.

## 📌 Project Overview

This project is a small Flask application that exposes product data through HTTP endpoints.

The main goal is to practice:

* Flask Application setup
* Routing
* HTTP GET requests
* Query Parameters
* Request handling
* JSON responses
* HTML responses
* Jinja2 Templates
* Basic data filtering

The project uses an in-memory Python list as its data source, so no database is required.

---

## 🛠️ Technologies

* **Python**
* **Flask**
* **HTML**
* **Jinja2**

---

## 📁 Project Structure

```text
mini_data_api/
│
├── app.py
├── data.py
├── README.md
│
└── templates/
    └── products.html
```

### `app.py`

Contains the Flask application, routes, request handling, and response logic.

### `data.py`

Contains the product data used by the application.

### `templates/products.html`

HTML template used to display products in the browser.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Navigate to the Project

```bash
cd mini_data_api
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

The application will run locally on:

```text
http://127.0.0.1:5000
```

---

## 🔗 API Endpoints

### GET `/`

Returns a simple welcome message.

```text
GET /
```

Example:

```text
http://127.0.0.1:5000/
```

---

### GET `/products`

Returns all available products as an HTML page.

```text
GET /products
```

Example:

```text
http://127.0.0.1:5000/products
```

---

### GET `/products?id=<id>`

Returns a specific product based on its ID.

Example:

```text
GET /products?id=2
```

URL:

```text
http://127.0.0.1:5000/products?id=2
```

The application reads the `id` from the query parameter and filters the product data.

---

## 📊 Example Data

The application currently contains products such as:

| ID | Name         | Category    | Price |
| -: | ------------ | ----------- | ----: |
|  1 | Laptop       | Electronics | 25000 |
|  2 | Keyboard     | Electronics |   800 |
|  3 | Office Chair | Furniture   |  4500 |
|  4 | Notebook     | Stationery  |   120 |
|  5 | Mouse        | Electronics |   600 |

---

## 🧠 Concepts Practiced

This project was created as a practical exercise to understand how Flask handles a basic request-response cycle:

```text
Client
   │
   │ HTTP Request
   ▼
Flask Application
   │
   │ Route Matching
   ▼
Python Function
   │
   │ Data Processing
   ▼
Response
   │
   ▼
Client
```

The project specifically demonstrates:

* Flask Application Object
* Routes
* GET requests
* Query Parameters
* `request.args`
* Type conversion
* Basic filtering
* `render_template()`
* Jinja2 template rendering
* HTML responses
* Local Flask development server

---

## 🎯 Project Scope

This project intentionally focuses on **Flask fundamentals** rather than advanced backend development.

It does not currently include:

* Database integration
* Authentication
* Authorization
* JWT
* Blueprints
* Docker
* Cloud deployment
* Advanced API architecture

These features can be introduced in future projects as Flask knowledge develops.

---

## 🔮 Possible Future Improvements

Possible extensions include:

* Add POST requests to create products
* Add PUT requests to update products
* Add DELETE requests
* Add JSON request bodies
* Add input validation
* Add HTTP status codes
* Add category filtering
* Add sorting
* Add database integration
* Add basic API testing

---

## 👨‍💻 Author

**Ahmed Ibrahim**

Computer and Data Science Student
Aspiring Junior Data Engineer

---

## 📄 License

This project is created for learning and portfolio purposes.
