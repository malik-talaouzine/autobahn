# 🚧 Autobahn Map Viewer

An interactive web dashboard that visualizes real-time Autobahn (German highway) data on a map. It fetches information from [autobahn.api.bund.dev](https://autobahn.api.bund.dev/) and stores it in a MySQL database. Data includes service stations, lorry parking, closures, warnings, and roadworks — all shown on a Leaflet.js map.

---

## 🌟 Features

- 🗺️ Interactive Leaflet map using OpenStreetMap tiles
- ✅ Toggleable data layers:
  - 🚉 Service Stations
  - 🚛 Lorry Parking
  - 🚧 Road Closures
  - ⚠️ Traffic Warnings
  - 🔨 Roadworks
- 🔄 Periodic data fetching and DB sync
- 💾 Data persistence in MySQL
- 🧩 Modular Django templates and static assets

---

## 🐳 Quick Start with Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/autobahn-map.git
cd autobahn-map
```

### 2. Create a .env file
DB=db
USER=root
PASSWORD=<your-password>
ROOTPW=<your-root-password>
PORT=3306
HOST=mysql-container

### 3. Start the App
docker-compose up --build

This will:

Build the Django app container

Start a MySQL database

Serve the map on port 8000

### 4. Apply Migrations
docker exec -it django-container bash
python manage.py makemigrations
python manage.py migrate

### 5. Visit the App
App UI: http://localhost:8000

