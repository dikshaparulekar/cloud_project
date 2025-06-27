Weather Forecast App using Flask and Google Cloud

A live weather forecast web app built with Python Flask, using the OpenWeather API and deployed on Google Cloud Run. It stores the results in Google Cloud SQL (MySQL).

Features:
- Search live weather by city name
- Uses OpenWeatherMap API for real-time data
- Built with Python Flask
- Containerized with Docker
- Deployed to Google Cloud Run
- Stores results in Google Cloud SQL
- GitHub-integrated CI/CD using Cloud Build

Live Demo:
App URL: https://your-cloud-run-url.a.run.app

Technologies & GCP Services Used:
- Python Flask (backend)
- HTML (frontend with Jinja2)
- Docker (containerization)
- Google Cloud Run (hosting)
- Cloud SQL (MySQL) (database)
- Cloud Build (CI/CD automation)
- Artifact Registry (stores Docker image)
- Cloud Shell & Logging (debug & SQL access)
- GitHub (version control)
- OpenWeatherMap API

Project Structure:
weather-app/
├── app.py
├── var.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html

Run Locally:
git clone https://github.com/dikshaparulekar/cloud_project.git
cd cloud_project
pip install -r requirements.txt
python app.py

Status:
Project is complete and deployed on Google Cloud Run.

Author: Diksha Parulekar
