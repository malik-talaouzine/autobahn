# 🚧 Autobahn Map Viewer

An interactive web dashboard that visualizes real-time Autobahn (German highway) data on a map. It fetches information from [autobahn.api.bund.dev](https://autobahn.api.bund.dev/) and stores it in a MySQL database. Data includes service stations, lorry parking, closures, warnings, and roadworks — all shown on a Leaflet.js map.

You can **click on any element** displayed on the map (such as service stations, lorry parking, closures, etc.) to get more information about it!

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
- 🔍 **Click on any map element** to view detailed information about it

---

## 🐳 Quick Start with Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/malik-talaouzine/autobahn.git
cd autobahn

```

### 2. Create a .env file
```bash
DB=db
USER=root
PASSWORD=<your-password>
ROOTPW=<your-root-password>
PORT=3306
HOST=mysql-container
```

### 3. Start the App
```bash
docker-compose up --build
```

This will:

Build the Django app container
Start a MySQL database
Apply the migrations
Serve the map on port 8000

### 4. Visit the App
App UI: http://localhost:8000

