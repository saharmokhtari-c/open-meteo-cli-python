# 🌤️ Open-Meteo Weather CLI
A lightweight Command-Line Interface (CLI) tool built with Python to fetch and display current weather data using the Open-Meteo API.
The project supports containerization using Docker for seamless setup and execution.
---
## 🚀 Features
* *Fetch Real-time Data:* Get current weather parameters for multiple cities at once.
* *CLI Arguments:* Pass city names directly via command-line arguments.
* *Error Handling:* Graceful handling of invalid city names and network connection errors.
* *Dockerized:* Fully containerized environment for easy execution without manually managing Python dependencies.
---
## 🛠️ Tech Stack
* *Language:* Python 3.x
* *Libraries:* requests
* *API:* Open-Meteo Geocoding & Weather API
* *DevOps:* Docker
---
## 🖥️ How to Run Locally

### Prerequisites
* Python 3.10+ installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/saharmokhtari-c/open-meteo-cli-python.git
   cd open-meteo-cli-python

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   python main.py milan turin tehran
---
### How to Run with Docker
You can run this project using Docker without installing Python dependencies on your system.
1. Build the Docker image:
   ```bash
   docker build -t open-meteo-cli
2. Run the container:
   ```bash
   docker run --rm open-meteo-cli milan turin tehran

Developed by Sahar Mokhtari






