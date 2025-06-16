# 🚧 Autobahn Map Viewer

An interactive web dashboard that visualizes real-time Autobahn (German highway) data on a map. It fetches information from [autobahn.api.bund.dev](https://autobahn.api.bund.dev/) and stores it in a MySQL database. Data includes service stations, lorry parking, closures, warnings, and roadworks — all shown on a Leaflet.js map.

You can **click on any element** displayed on the map (such as electric charging stations, lorry parking, closures, etc.) to get more information about it!

---

## 🌟 Features

- 🗺️ Interactive Leaflet map using OpenStreetMap tiles
- ✅ Toggleable data layers:
  - 🚉 Electric Charging Stations
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

### 2. Create your own .env file
```bash
DB=<your-db-name>
USER=<your-username>
PASSWORD=<your-password>
HOST=<your-hostname>
PORT=3306
```
or just copy this example:
```bash
DB=db
USER=test
PASSWORD=password
HOST=mysql-container
PORT=3306
```

### 3. Start the App
```bash
docker-compose up --build
```

This will:

- Build the Django app container
- Start a MySQL database
- Apply the migrations
- Update the data
- Serve the map on port 8000

### 4. Visit the App
If this is your first time starting the project it will take a few minutes before you can use the interactive map!
App UI: http://localhost:8000

